import os
import click
import shutil
from rich import print


def copy_ffhq_model(dataset_name, model_path='model/ffhq.pkl'):
    """Copy FFHQ model to new dataset loc."""
    real_path = os.path.realpath(model_path)
    dir_path = os.path.dirname(real_path)
    new_path = os.path.join(dir_path, dataset_name + '.pkl')
    shutil.copyfile(real_path, new_path)


@click.command()
@click.option(
    '--dataset_name',
    '-d',
    required=True
)
@click.option(
    '--model_path',
    default='model/ffhq.pkl'
)
def main(dataset_name, model_path):
    print(f'Getting model from {model_path} for new dataset {dataset_name}')
    copy_ffhq_model(dataset_name, model_path)


if __name__ == '__main__':
    main()
