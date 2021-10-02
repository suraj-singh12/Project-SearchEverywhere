# Contributing

1. Fork the repository

2. Clone the repo to your local system
```bash
  git clone https://github.com/<your-user-name>/Project-SearchEverywhere.git
```
```bash  
  cd Project-SearchEverywhere
```

3. Install dependencies 
* [debian-based]
```bash
  sudo sh debiandep.sh
```
* [arch-based]
```bash
  sudo sh fedoradep.sh
```

4. Make the source file executable
```bash
  chmod +x src/SearchEverywhere.py
```

5. Copy the src/ contents to testing_base/
```bash
  cp -R src/* testing_base/
```
```bash
 cd testing_base/
```

6. Conduct tests using source file (```SearchEverywhere.py```) in testing_base directory, for example:
```bash
  ./SearchEverywhere.py - heading
```
7. Create a new branch before making any changes to source file ```SearchEverywhere.py``` in ```src/```

8. Commit your final changes (bug fix/feature added etc.) in ```src/SearchEverywhere.py``` with an appopriate comment expaining the change.

9. Create a pull request for ```src/SearchEverywhere.py``` script only.

10. Thank You, your PR will be looked upon soon.

> Kindly consider testing and debugging on a bunch of files of different file types(.txt, .odp, .odt, .pdf) to ensure that nothing is broken by the change made by you.
