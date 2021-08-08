import os
import cv2
import click
from rich import print


def write_frames(mp4_path, output_path):
    vc = cv2.VideoCapture(mp4_path)
    c = 1

    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False
        print('No frames found...')

    base = os.path.basename(mp4_path)
    scene_name = os.path.splitext(base)[0]
    base_fpath = os.path.join(output_path, scene_name + '_')

    print(f'Saving as {base_fpath}')

    while rval:
        rval, frame = vc.read()

        try:
            cv2.imwrite(base_fpath + str(c) + '.jpg', frame)
            c = c + 1
            cv2.waitKey(1)
        except cv2.error as ex:
            print(ex)
            print('Done!')
    vc.release()


@click.command()
@click.option(
    '--input',
    '-i',
    help='Input file to extract frames from.'
)
@click.option(
    '--output',
    '-o',
    help='Output folder.'
)
def main(input, output):
    write_frames(input, output)


if __name__ == '__main__':
    main()
