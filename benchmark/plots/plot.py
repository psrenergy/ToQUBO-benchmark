import matplotlib.pyplot as plt
import scienceplots
from pandas import read_csv
from pathlib import Path

BASE_PATH = Path.cwd().joinpath("benchmark")

plt.rcParams.update({
    "text.usetex" : True
})

def plot_benchmark():
    toqubo_data         = read_csv(BASE_PATH.joinpath("ToQUBO"    , "results.csv"))
    pyqubo_current_data = read_csv(BASE_PATH.joinpath("pyqubo"    , "results.csv"))
    pyqubo_040_data     = read_csv(BASE_PATH.joinpath("pyqubo_040", "results.csv"))
    qubovert_data       = read_csv(BASE_PATH.joinpath("qubovert"  , "results.csv"))

    plt.figure(figsize = (5,4))

    plt.style.use(['science'])

    # plt.plot(
    #     toqubo_data["nvar"],
    #     toqubo_data["toqubo_time"],
    #     label = r"ToQUBO$^\dagger$ 0.1.4",
    #     marker='o'
    # )
    plt.plot(
        pyqubo_040_data["nvar"],
        pyqubo_040_data["time"],
        label  = r"\texttt{PyQUBO 0.4.0}",
        color  = "#2a838a", # PSRLIGHTGREEN
        marker = 'o',
    )
    plt.plot(
        qubovert_data["nvar"],
        qubovert_data["time"],
        label  = r"\texttt{qubovert 1.2.5}",
        color  = "#546670", # PSRGRAY
        marker ='o',
    )
    plt.plot(
        pyqubo_current_data["nvar"],
        pyqubo_current_data["time"],
        label  = r"\texttt{PyQUBO 1.4.0}",
        color  = "#002846", # PSRBLUE
        marker ='o',
    )
    plt.plot(
        toqubo_data["nvar"],
        toqubo_data["time"],
        label  = r"\texttt{ToQUBO.jl 0.1.4}",
        color  ="#a49375", # PSRGOLD
        marker ='o',
    )

    plt.xscale('symlog')
    plt.yscale('symlog')
    plt.xlabel(r"\texttt{\#variables}")
    plt.ylabel("Building Time (sec)")
    plt.grid(True)

    # Reorder Legend
    handles, labels = plt.gca().get_legend_handles_labels()
    legend_order    = [3,2,0,1]

    plt.legend(
        [handles[i] for i in legend_order],
        [labels[i]  for i in legend_order],
    )

    plt.savefig(str(BASE_PATH.joinpath("benchmark.pdf")))

    return None

def plot_toqubo():
    toqubo_data = read_csv(BASE_PATH.joinpath("ToQUBO", "results.csv"))

    plt.figure(figsize = (5,4))

    plt.style.use(['science'])

    plt.plot(toqubo_data["nvar"], toqubo_data["toqubo_time"], label = "ToQUBO", marker='D')
    plt.plot(toqubo_data["nvar"], toqubo_data["jump_time"]  , label = "JuMP"  , marker='D')
    plt.xscale('symlog')
    plt.yscale('symlog')
    plt.xlabel(r"\#variables")
    plt.ylabel("Running Time (sec)")
    plt.grid(True)
    plt.legend()

    plt.savefig(str(BASE_PATH.joinpath("toqubo.pdf")))

    return None

if __name__ == "__main__":
    plot_benchmark()
    plot_toqubo()