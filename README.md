# ci-lab-app

A small Python string-stats library plus a GitHub Actions workflow that runs
pytest on pull requests — built to exercise DevFoundry's CI repair.

- Library: `stats.py` (`word_count`, `initials`, `slugify`, `reverse_words`).
- Tests: `test/test_stats.py` (unittest, pytest-compatible).
- CI: `.github/workflows/pytest.yml` runs the tests on pull requests.
- Run tests with `python3 -m unittest discover -s . -t .` (or `bash check.sh`).
