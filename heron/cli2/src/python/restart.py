#!/usr/bin/python2.7

import argparse
import atexit
import base64
import contextlib
import glob
import logging
import logging.handlers
import os
import shutil
import sys
import subprocess
import tarfile
import tempfile

import heron.cli2.src.python.args as args

def create_parser(subparsers):
  parser = subparsers.add_parser(
      'restart', 
      help='Restart a topology',
      usage = "%(prog)s [options] config-overrides topology-name [shard-identifier]",
      add_help = False)

  args.add_titles(parser)
  args.add_config_overrides(parser)
  args.add_topology(parser)

  parser.add_argument(
      'shard-identifier', 
      nargs='?', 
      type=int, 
      default=-1, 
      help='Identifier of the shard to be restarted')

  args.add_config(parser)
  args.add_verbose(parser)

  parser.set_defaults(subcommand='activate')
  return parser

def execute(parser, args, unknown_args):
  pass
