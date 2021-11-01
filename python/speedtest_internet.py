#Speed Test using Python
# pip install speedtest-cli
import speedtest_cli
sp = speedtest.Speedtest()
print(f"Download Speed : { sp.download()}")
print(f"Upload Speed : { sp.upload()}")