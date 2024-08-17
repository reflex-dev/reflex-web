# test.py
import cProfile

profiler = cProfile.Profile()
profiler.enable()
print("Profiling...")
import pcweb.pcweb # You can put any code here that you want to profile
pcweb.pcweb.app._compile()
print("Done profiling.")

# Stop profiling
profiler.disable()

# Save the profile data to a file
profiler.dump_stats('myprofile.prof')