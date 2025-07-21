## DONE:
- [X]  Create C files for compiled binary to be reverse engineered for levels 1-4
- [X]  Create python scripts to test the hacker's reconstructed files
- [X]  Set up the basic levels 1-4 and get them working to some degree (can get the flag somehow)

## TO-DO:
- [ ]  Make it so the python script is not readable to the hacker user
- [ ]  Fix the permissions issue with python script  
        * Does not work without sudo  
        * Seems to be an issue with python scripts being interpreted instead of compiled?
- [ ]  Fix the issue of needing python3 to run the RunTest.py scripts on the levels  
        * \r character issue seems to be some sort of windows and linux system char misalignment? Need to investigate further
- [ ]  Add more levels  
        * Challenges where the user must compile their own C file for testing (Perhaps problem that requires using special gcc flags?) 
        * Challenge with multiple C files that interact that must be reverse engineered  
        * Challenge where users must reverse engineer what different C files do and how they interact              in order to create a MakeFile that links them correctly (Maybe build order dependency or something like that)  
        * Header file reverse engineering challenge where binary requries a header #include that must              be reverse engineered  
        * Library .so file reverse engineer problem where user must reverse engineer what the missing              library file does and reconstruct it


## PROGRESS LOG:
**21 July 2025 - 4:25 P.M.**  
The basic levels 1-4 have been set up with the compiled binary to be reversed engineered alongside the python scripts that tests the hacker user's reconstructed C file, and am able to get the flag in practice mode. There are still issues to be addressed (see TO-DO)
