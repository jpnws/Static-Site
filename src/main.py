import pathlib
import os
import shutil
from copystatic import directory_copier
from page_generator import generate_pages_recursive


def main():
    content = pathlib.Path(
        os.path.abspath(os.path.expanduser(os.path.expandvars("./static_site/content")))
    )
    static = pathlib.Path(
        os.path.abspath(os.path.expanduser(os.path.expandvars("./static_site/static")))
    )
    template = pathlib.Path(
        os.path.abspath(
            os.path.expanduser(os.path.expandvars("./static_site/template.html"))
        )
    )
    dest_path = pathlib.Path(
        os.path.abspath(os.path.expanduser(os.path.expandvars("./static_site/public")))
    )
    print(f"Setting up directory at {dest_path}")
    if os.path.exists(dest_path):
        print("Removing old files")
        shutil.rmtree(dest_path)
        print("Creating files:")
    directory_copier(static, dest_path)  # type: ignore
    generate_pages_recursive(content, template, dest_path)  # type: ignore


main()
