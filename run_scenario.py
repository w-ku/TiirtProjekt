import subprocess
import os
import sys

def run(scenario_name):
    f = open("scenarios/" + scenario_name + ".txt", "r")
    out_d = open("scenarios/" + scenario_name + "_d.txt", "w")
    out_pb = open("scenarios/" + scenario_name + "_pb.txt", "w")

    for line in f:
        cmd = "python __init__.py --debug 0 " + line
        print "Running: " + cmd
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        result = out.split('\n')

        for l in result:
            if l.startswith("SREDNI CZAS OCZEKIWANIA: "):
                out_d.write(l.replace("SREDNI CZAS OCZEKIWANIA: ", ""))
                out_d.write(os.linesep) 
            if l.startswith("PRAWDOPODOBIENSTWO ODRZUCENIA: "):
                out_pb.write(l.replace("PRAWDOPODOBIENSTWO ODRZUCENIA: ", ""))
                out_pb.write(os.linesep) 

    f.close()
    out_d.close()
    out_pb.close()

    print "Results for " + f.name + ":\n" + out_d.name + "\n" + out_pb.name


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Proper use: python run_scenario.py SCENARIO_NAME\nwhere SCENARIO_NAME is a text file placed in the scenario subdir.\n\nEXAMPLE: python run_scenario.py scenario_0"
        sys.exit()
    run(sys.argv[1])
