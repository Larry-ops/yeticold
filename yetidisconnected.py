import subprocess
import os

if not (os.system("python3 -c 'import flask'") == 0):
	subprocess.call(['bash -c "sudo chmod +x ~/yeticold/dpkg-script.sh; sudo ~/yeticold/dpkg-script.sh"'],shell=True)
subprocess.call(['sudo chmod +x ~/yeticold/bitcoin-0.19.0rc1/bin/bitcoin-cli'],shell=True)
subprocess.call(['sudo chmod +x ~/yeticold/bitcoin-0.19.0rc1/bin/bitcoind'],shell=True)
subprocess.call(['sudo chmod +x ~/yeticold/bitcoin-0.19.0rc1/bin/bitcoin-qt'],shell=True)
subprocess.call(['sudo chmod +x ~/yeticold/bitcoin-0.19.0rc1/bin/bitcoin-wallet'],shell=True)
subprocess.call(['sudo chmod +x ~/yeticold/bitcoin-0.19.0rc1/bin/bitcoin-tx'],shell=True)
subprocess.call('sudo rm -r ~/.bitcoin/full0', shell=True)
subprocess.call('sudo rm -r ~/.bitcoin/full1', shell=True)
subprocess.call('sudo rm -r ~/.bitcoin/full2', shell=True)
subprocess.call('sudo rm -r ~/.bitcoin/full3', shell=True)
subprocess.call('sudo rm -r ~/.bitcoin/full4', shell=True)
subprocess.call('sudo rm -r ~/.bitcoin/full5', shell=True)
subprocess.call('sudo rm -r ~/.bitcoin/full6', shell=True)
subprocess.call('sudo rm -r ~/.bitcoin/blank0', shell=True)
subprocess.call('sudo rm -r ~/.bitcoin/blank1', shell=True)
subprocess.call('sudo rm -r ~/.bitcoin/blank2', shell=True)
subprocess.call('sudo rm -r ~/.bitcoin/blank3', shell=True)
subprocess.call('sudo rm -r ~/.bitcoin/blank4', shell=True)
subprocess.call('sudo rm -r ~/.bitcoin/blank5', shell=True)
subprocess.call('sudo rm -r ~/.bitcoin/blank6', shell=True)
subprocess.call('sudo rm ~/.bitcoin/wallet.dat', shell=True)
subprocess.call('sudo rm ~/.bitcoin/.walletlock', shell=True)
subprocess.call('sudo rm ~/full0', shell=True)
subprocess.call('sudo rm ~/full1', shell=True)
subprocess.call('sudo rm ~/full2', shell=True)
subprocess.call('sudo rm ~/full3', shell=True)
subprocess.call('sudo rm ~/full4', shell=True)
subprocess.call('sudo rm ~/full5', shell=True)
subprocess.call('sudo rm ~/full6', shell=True)
subprocess.call('sudo rm ~/blank0', shell=True)
subprocess.call('sudo rm ~/blank1', shell=True)
subprocess.call('sudo rm ~/blank2', shell=True)
subprocess.call('sudo rm ~/blank3', shell=True)
subprocess.call('sudo rm ~/blank4', shell=True)
subprocess.call('sudo rm ~/blank5', shell=True)
subprocess.call('sudo rm ~/blank6', shell=True)
subprocess.Popen('python3 ~/yeticold/hello.py',shell=True,start_new_session=True)
subprocess.call(['xdg-open http://localhost:5000/step15'],shell=True)
