import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Conway's Game of Life",
    options={"build_exe": {"packages":["pygame"],
                           }},
    executables = executables

    )