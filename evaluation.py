import os
import shutil


# testing datasets
# testing_datasets = ["HE", "HE_ET", "MBPP", "MBPP_ET"]
testing_datasets = ["MBPP_ET"]


# run evaluation on each dataset
for dataset in testing_datasets:
    # list all corresponding dataset files in folder "cases" and sort
    if dataset == "HE" or dataset == "HE_ET":
        files = [f for f in os.listdir("./cases_KB_HE") if "HE" in f]
    else:
        files = [f for f in os.listdir("./cases_CI+KB_MBPP") if "MBPP" in f]
    files.sort()

    # for each project in "cases", copy source code and testcase to result and run test, save success/failure in a list
    success = []
    failure = []
    for file in files:
        # extract case prefix
        case_prefix = file.split(".")[0]

        # create project folder
        project_folder = os.path.join(f"{os.environ['PWD']}", "results", case_prefix)
        if not os.path.exists(project_folder):
            os.makedirs(project_folder)
        os.chdir(project_folder)

        # copy source code to project folder
        shutil.copy(os.path.join(f"{os.environ['PWD']}", "cases_CI+KB_MBPP", file), project_folder)

        # find test case file
        case_number = case_prefix.split("_")[-1]
        test_case_file = os.path.join(f"{os.environ['PWD']}", "test_cases", f"{dataset}", f"testcase_{case_number}.py")

        # copy test file to project folder
        shutil.copy2(test_case_file, os.path.join(project_folder, f"testcase_{dataset}_{case_number}.py"))

        # run test file
        run_code = os.system(f"python testcase_{dataset}_{case_number}.py")
        if run_code == 0:
            print(f"\033[92m{case_number} success\033[0m")
            success.append(case_number)
        else:
            print(f"\033[91m{case_number} failure\033[0m")
            failure.append(case_number)

    # print success/failure
    print(f"Dataset: {dataset}:")
    print(f"success: {success}")
    print(f"failure: {failure}")
    os.chdir(os.environ['PWD'])
