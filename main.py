import argparse

from moviepy.editor import CompositeVideoClip, VideoFileClip


def make_parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--base",
        default="inputs/base.mp4",
        type=str,
        help="movie of person speaking",
    )
    parser.add_argument(
        "--slide",
        default="inputs/slide.mov",
        type=str,
        help="movie of slide",
    )
    parser.add_argument(
        "--save",
        default="outputs/work.mp4",
        type=str,
        help="plese set path for saving",
    )
    parser.add_argument(
        "--ratio",
        default=0.5,
        type=float,
        help="plese set slide ratio",
    )
    parser.add_argument(
        "--time",
        default=35.0,
        type=float,
        help="plese set time to finish",
    )

    return parser.parse_args()


def main():
    args = make_parse()

    base = VideoFileClip(args.base)
    w, h = base.size
    audioclip = base.audio

    wipe = (
        VideoFileClip(args.slide)
        .resize((w * args.ratio, h * args.ratio))
        .margin(6, color=(255, 255, 255))
        .margin(left=50, opacity=0)
        .set_pos(("left", "center"))
    )

    work = CompositeVideoClip([base, wipe])
    work.set_audio(audioclip)
    work.subclip(0, args.time).write_videofile(
        args.save,
        codec="libx264",
        audio_codec="aac",
        temp_audiofile="temp-audio.mp3",
        remove_temp=True,
    )


if __name__ == "__main__":
    main()
