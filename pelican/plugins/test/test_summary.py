import pathlib

import pytest

import pelican


@pytest.fixture(scope="module", autouse=True)
def site(tmp_path_factory):
    output = tmp_path_factory.getbasetemp()
    datadir = pathlib.Path(__file__).parent / "data"
    args = [
        datadir / "content",
        "-o",
        output,
        "-s",
        datadir / "pelicanconf.py",
        "--relative-urls",
    ]
    pelican.main([str(a) for a in args])
    yield output


def test_show_source(site):
    tag = "esse-quam-laboriosam-at-accusantium"

    # verify the pages have been created
    assert (site / (tag + ".html")).exists()
    assert (site / (tag + "-ii.html")).exists()


    # verify presence of summaries in the rendered index
    text = (site / "index.html").read_text()

    assert "This is the summary line for the first article." in text
    assert "This is the summary line for the second article." in text
