import subprocess

SET_DESKTOP_IMAGE_WRAPPER = """/usr/bin/osascript<<END
tell application "System Events"
{}
end tell
END"""

SET_DESKTOP_IMAGE = """
set currDesktop to item {idx} of desktops
set currDesktop's picture to "{image_path}"
"""

def set_wallpapers(images):
    # images is an array of file paths of desktops

    script_contents = ""
    for i, img in enumerate(images):
        index = i+1
        script_contents += SET_DESKTOP_IMAGE.format(idx=index, image_path=img)

    script = SET_DESKTOP_IMAGE_WRAPPER.format(script_contents)
    subprocess.check_call(script, shell=True)

    # Kill Dock process to apply changes
    subprocess.check_call("killall Dock", shell=True)