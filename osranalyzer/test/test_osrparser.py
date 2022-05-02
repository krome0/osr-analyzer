from osrparse import Replay, parse_replay_data

replay = Replay.from_path('test_osr_ss.osr')

r = replay
print(r.timestamp)