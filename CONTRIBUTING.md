# Contributing

1. Fork the repository
```bash
  git clone https://github.com/suraj-singh12/Project-SearchEverywhere.git
```
```bash  
  cd Project-SearchEverywhere
```

2. Install dependencies
```bash
  sudo chmod +x dependencies.sh
```
```bash
  sudo ./dependencies.sh
```

3. Copy the src/ contents to testing_base/
```bash
  cp -R source/* testing_base/
```
```bash
 cd testing_base/
```

4. Conduct tests using source file (```SearchEverywhere.py```) in testing_base directory, for example:
```bash
  ./SearchEverywhere.py - heading
```

5. Create a new branch before making any changes to source file ```SearchEverywhere.py``` in ```src/```

6. Commit your final changes (bug fix/feature added etc.) in ```src/SearchEverywhere.py``` with an appopriate comment expaining the change.

7. Create a pull request for ```src/SearchEverywhere.py``` script only.

8. Thank You, your PR will be looked upon soon.

> Kindly consider testing and debugging on a bunch of files of different file types(.txt, .odp, .odt, .pdf) to ensure that nothing is broken by the change made by you.
