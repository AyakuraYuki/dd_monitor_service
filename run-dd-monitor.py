# -*- coding: utf-8 -*-

import fire

from app.app import app


def run(port: int = 5140):
    app.run(
        port=port
    )


if __name__ == '__main__':
    fire.Fire(run)
