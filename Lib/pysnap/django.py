from __future__ import absolute_import
from django.test import TestCase as dTestCase
from django.test import SimpleTestCase as dSimpleTestCase
from django.test.runner import DiscoverRunner

from pysnap.reporting import reporting_lines
from .unittest import TestCase as uTestCase
from .module import SnapshotModule


class TestRunner(DiscoverRunner):

    separator1 = "=" * 70
    separator2 = "-" * 70

    def __init__(self, snapshot_update=False, **kwargs):
        super(TestRunner, self).__init__(**kwargs)
        uTestCase.snapshot_should_update = snapshot_update

    @classmethod
    def add_arguments(cls, parser):
        super(TestRunner, cls).add_arguments(parser)
        parser.add_argument(
            '--snapshot-update', default=False, action='store_true',
            dest='snapshot_update', help='Update the snapshots automatically.',
        )

    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        result = super(TestRunner, self).run_tests(
                test_labels=test_labels,
                extra_tests=extra_tests,
                **kwargs
        )
        self.print_report()
        if TestCase.snapshot_should_update:
            for module in SnapshotModule.get_modules():
                module.delete_unvisited()
                module.save()

        return result

    def print_report(self):
        print("\n" + self.separator1)
        print('PySnap summary')
        print(self.separator2)
        for line in reporting_lines('python manage.py test'):
            print(line)
        print(self.separator1)


class TestCase(uTestCase, dTestCase):
    pass


class SimpleTestCase(uTestCase, dSimpleTestCase):
    pass
