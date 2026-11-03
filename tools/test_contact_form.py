#!/usr/bin/env python3
"""Behaviour tests for the electronics-website contact form (mailto hand-off).

Copied from the shared tools/behaviour_test_template.py; the runner is unchanged.

    python tools/test_contact_form.py              # tests ./index.html
    python tools/test_contact_form.py --page <url> # tests the live preview

Exit codes: 0 every test passed, 1 a test failed or Chromium could not launch,
2 the page was not found.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.parse import unquote


# --- the tests -------------------------------------------------------------

def _fill_valid(page) -> None:
    page.get_by_test_id("contact-name").fill("Ana Pop")
    page.get_by_test_id("contact-company").fill("A&B Components")
    page.get_by_test_id("contact-email").fill("ana@example.com")
    page.get_by_test_id("contact-message").fill("Quote for 500 units?")


def test_empty_submit_flags_every_required_field(page, expect) -> None:
    page.get_by_test_id("contact-submit").click()
    for field in ("name", "email", "message"):
        expect(page.get_by_test_id(f"contact-{field}")).to_have_attribute("aria-invalid", "true")
        expect(page.get_by_test_id(f"contact-{field}-error")).to_be_visible()
    expect(page.get_by_test_id("contact-name")).to_be_focused()
    expect(page.get_by_test_id("contact-status")).to_be_hidden()


def test_invalid_email_is_rejected(page, expect) -> None:
    _fill_valid(page)
    page.get_by_test_id("contact-email").fill("ana@")
    page.get_by_test_id("contact-submit").click()
    expect(page.get_by_test_id("contact-email-error")).to_be_visible()
    expect(page.get_by_test_id("contact-status")).to_be_hidden()


def test_fixing_a_field_clears_its_error(page, expect) -> None:
    page.get_by_test_id("contact-submit").click()
    page.get_by_test_id("contact-name").fill("Ana")
    expect(page.get_by_test_id("contact-name")).to_have_attribute("aria-invalid", "false")
    expect(page.get_by_test_id("contact-name-error")).to_be_hidden()


def test_valid_submit_builds_a_complete_mailto_and_shows_status(page, expect) -> None:
    _fill_valid(page)
    page.get_by_test_id("contact-submit").click()
    expect(page.get_by_test_id("contact-status")).to_be_visible()
    href = unquote(page.get_by_test_id("contact-form").get_attribute("data-mailto"))
    # An unencoded "&" in the company used to cut the body off here.
    for part in ("mailto:andrei@westpointeurope.com", "Company: A&B Components",
                 "Email: ana@example.com", "Quote for 500 units?"):
        if part not in href:
            raise AssertionError(f"mailto is missing {part!r}")


def test_write_another_restores_an_empty_form(page, expect) -> None:
    _fill_valid(page)
    page.get_by_test_id("contact-submit").click()
    page.get_by_test_id("contact-reset").click()
    expect(page.get_by_test_id("contact-form")).to_be_visible()
    expect(page.get_by_test_id("contact-name")).to_have_value("")
    expect(page.get_by_test_id("contact-name")).to_be_focused()


def test_mobile_menu_opens_and_closes_with_escape(page, expect) -> None:
    page.set_viewport_size({"width": 375, "height": 800})
    toggle = page.get_by_test_id("nav-toggle")
    toggle.click()
    expect(toggle).to_have_attribute("aria-expanded", "true")
    expect(page.get_by_test_id("nav-contact")).to_be_visible()
    page.keyboard.press("Escape")
    expect(toggle).to_have_attribute("aria-expanded", "false")
    expect(toggle).to_be_focused()


TESTS = [
    test_empty_submit_flags_every_required_field,
    test_invalid_email_is_rejected,
    test_fixing_a_field_clears_its_error,
    test_valid_submit_builds_a_complete_mailto_and_shows_status,
    test_write_another_restores_an_empty_form,
    test_mobile_menu_opens_and_closes_with_escape,
]


# --- the runner — copy this part unchanged ---------------------------------

def run(url: str, tests: list) -> int:
    try:
        from playwright.sync_api import expect, sync_playwright
    except ImportError:
        print(
            "behaviour_test: Playwright (Python) is not importable. Report this "
            "check as NOT RUN. Fix with: python tools/web_doctor.py",
            file=sys.stderr,
        )
        return 1

    failures = []
    with sync_playwright() as pw:
        try:
            browser = pw.chromium.launch()
        except Exception as exc:  # noqa: BLE001 — a launch failure must be loud
            print(f"behaviour_test: Chromium failed to launch ({exc}).", file=sys.stderr)
            print("Report this check as NOT RUN. Fix with: python tools/web_doctor.py", file=sys.stderr)
            return 1
        try:
            for test in tests:
                page = browser.new_page()
                try:
                    page.goto(url, wait_until="load", timeout=30_000)
                    test(page, expect)
                    print(f"PASS  {test.__name__}")
                except Exception as exc:  # noqa: BLE001
                    failures.append(test.__name__)
                    first_line = str(exc).strip().splitlines()[0] if str(exc).strip() else type(exc).__name__
                    print(f"FAIL  {test.__name__}: {first_line}")
                finally:
                    page.close()
        finally:
            browser.close()

    print(f"\nbehaviour_test: {len(tests) - len(failures)}/{len(tests)} passed", file=sys.stderr)
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    parser = argparse.ArgumentParser(description="Contact form behaviour tests for electronics-website.")
    parser.add_argument(
        "--page",
        help="HTML file path or URL under test (default: this project's index.html)",
    )
    args = parser.parse_args(argv)

    if args.page and args.page.startswith(("http://", "https://")):
        url = args.page
    else:
        target = Path(args.page).expanduser().resolve() if args.page else Path(__file__).resolve().parent.parent / "index.html"
        if not target.exists():
            print(f"behaviour_test: page not found: {target}", file=sys.stderr)
            return 2
        url = target.as_uri()
    print(f"behaviour_test: contact form tests against {url}\n", file=sys.stderr)
    return run(url, TESTS)


if __name__ == "__main__":
    raise SystemExit(main())
