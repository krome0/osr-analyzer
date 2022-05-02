import osranalyzer.test.test_parser as test_parser
from datetime import datetime, timedelta

data = test_parser.load_file('test_osr_ss.osr')
parser = test_parser.Unpacker(data)
gamemode = parser.unpack_byte()
version = parser.unpack_int()
beatmap_hash = parser.unpack_string()
player_name = parser.unpack_string()
replay_hash = parser.unpack_string()
num_300 = parser.unpack_short()
num_100 = parser.unpack_short()
num_50 = parser.unpack_short()
num_gekis = parser.unpack_short()
num_katus = parser.unpack_short()
num_miss = parser.unpack_short()
score = parser.unpack_int()
combo = parser.unpack_short()
perfect = parser.unpack_byte()
mods = parser.unpack_int()
life_bar = parser.unpack_string()
time_tick = parser.unpack_ullong()
time_stamp = datetime.min+timedelta(microseconds=time_tick/10)  # centuryBegin + timespaned
replay_length = parser.unpack_int()

print(beatmap_hash, player_name, replay_hash)
print(life_bar)
print(time_stamp)
print(replay_length)