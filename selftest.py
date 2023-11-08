#!/usr/bin/env python3
"""Monitor a set of machines, sending an e-mail notification if one goes down."""

import argparse
import logging
import sys

log = logging.getLogger(__name__)

#######################################################################
# Main

def main():
    """Main program execution."""
    LOG_FORMAT = '%(levelname)s: %(message)s'
    LOG_LEVELS = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']

    parser = argparse.ArgumentParser(description='monitor machines and URLs for downtime')
    parser.add_argument('--log-level', type=str.upper, default='INFO', choices=LOG_LEVELS,
                        help='the desired logging level [INFO]')
    parser.add_argument('network',
                        help='network to examine')

    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(stream=sys.stdout, format=LOG_FORMAT, level=args.log_level)

    # Nothing real yet.
    log.info("PASS - no tests yest")
    return 0


#######################################################################
if __name__ == '__main__':
    sys.exit(main())
