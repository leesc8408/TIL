# 🚩Git / Github

## Git

- 분산버전관리시스템이다 
- 로컬의 파일 변경사항을 추적 / 여러 사용자간 작업 조율을 함

### 명령어 

- `git init`

  - git 으로 관리 할 수 있도록 레퍼로지토리(repository)를 만듬
    - 터미널 폴더경로에 (master)가 보이면 정상


---

- `git add`

  - 수정/생성한 파일을 스테이지(커밋예정)로 모음

    | 입력 코드         | 설명                        |
    | ----------------- | --------------------------- |
    | add 파일명.확장명 | 해당 파일만 스테이지로 모음 |
    | add .             | 모두 스테이지로 모음        |


---

- `git commit`

  - 스테이지에 모인걸 버전으로 남긴다

    | 입력 코드          | 설명                                         |
    | ------------------ | -------------------------------------------- |
    | commit -m '메세지' | 입력한 메세지를 기록하여 버전으로 남김(40자) |
    | commit             | 입력창이 활성화되며 40자 이상 기록가능       |


---

- `git status`
  - 커밋되기 전의 상태를 확인 가능

---

- `git log`

  - 커밋되어 기록된 버전을 확인

    | 입력 코드     | 설명                  |
    | ------------- | --------------------- |
    | log -1        | 최근 1가지 확인       |
    | log -2        | 최근 2가지 확인       |
    | log --oneline | 기록메세지만 간결하게 |

---

- `git config`

  - 사용자 정보 설정

    | 입력 코드                                 | 설명                      |
    | ----------------------------------------- | ------------------------- |
    | config --global user.name 'ID'            | 사용자 이름 설정          |
    | config --global user.email 'email'        | 사용자 이메일 설정        |
    | config --global --list                    | 등록된 사용자,이메일 확인 |
    | config --global core.editor "code --wait" | vscode를 에디터로 사용    |

---

- `git remote`

  - 원격저장소 명령어 (원격저장소이름: origin)

    | 입력 코드                              | 설명                         |
    | -------------------------------------- | ---------------------------- |
    | remote add origin https://원격저장주소 | 원격저장소주소를 로컬에 설정 |
    | remote -v                              | 설정된 원격 저장소 확인      |
    | remote remove origin                   | 설정된 원격 저장소 삭제      |

---

- `git push`

  - 로컬의 커밋된 버전을 원격저장소로 보내기(로컬->원격저장소)

    | 입력 코드                   | 설명                                       |
    | --------------------------- | ------------------------------------------ |
    | push origin master(or main) | 저장소이름(origin)에 브랜치(master / main) |

---

- `git pull`

  - 원격저장소의 버전을 로컬로 병합(로컬<-원격저장소)

    | 입력 코드                   | 설명                                       |
    | --------------------------- | ------------------------------------------ |
    | pull origin master(or main) | 저장소이름(origin)에 브랜치(master / main) |

---

- `git clone`

  - 원격저장소의 모든버전을 복제해서 가져옴

    | 입력 코드                    | 설명                                               |
    | ---------------------------- | -------------------------------------------------- |
    | clone https://원격저장소주소 | 원격저장소 이름의 폴더로 로컬의 현재 폴더에 가져옴 |

---

- `.gitignore`

  - 버전 관리가 필요없는 파일 / 폴더를 입력하여 목록에서 제외시킴

    > 처음 커밋하기전에 입력할것!!!!!(커밋된 이후에는 목록이 나옴. / 파일삭제 후 재 설정)

