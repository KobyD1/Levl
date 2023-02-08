import pytest

from Levl.Utils.eventsUtils import utils

pre_define_mac = "00:11:22:33:44:55"  # MAC address for failure in case it is loceted at position 10 or multiple of 10

utils = utils(pre_define_mac)

@pytest.mark.parametrize(
    'mac_none_10,position,desc',
    [
        ('00:01:02:03:04:55', 1, 'correct MAC'),
        ('00:01', 1, 'Short MAC'),
        ('00:01:02:03:04:05:06', 22, 'Long MAC'),
        ('00:01:02:03:04:WW', 1, 'Invalid digits'),
        (pre_define_mac, 5, 'Pre Define Mac'),
        (pre_define_mac, 9, 'Pre Define Mac at position 9'),
        (pre_define_mac, 11, 'Pre Define Mac at position 11'),

    ]
)
def test_none_10(mac_none_10, position, desc):
    mac_stream = utils.mac_stream_builder(mac_none_10, position, 30)
    utils.stream_validator(mac_stream)


@pytest.mark.parametrize(
    'mac_10,desc',
    [
        ('00:55:55:03:04:05', 'correct MAC'),
        ('00:01', 'Short MAC'),
        ('00:01:02:03:04:05:06', 'Long MAC'),
        ('00:01:02:03:04:WW', 'Invalid digits'),
        (pre_define_mac, 'Pre Define Mac'),
    ]
)
def test_Multiple_10(mac_10, desc):
    mac_stream = utils.mac_stream_builder(mac_10, 10, 14)
    utils.stream_validator(mac_stream)
