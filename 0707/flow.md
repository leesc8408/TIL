# git flow

> git을 활용하여 헙업하는 흐름으로 branch를 활용하는 전략

- 정답은 없다. 이용하는 서비스별 제안되는 흐름이 있으며,

  변형되어 프로젝트 / 회사에서 활용되고 있다.

- git flow에서 주요 사용되는 branch

  | branch                  | 설명                                                         |
  | ----------------------- | ------------------------------------------------------------ |
  | master(main)            | 배포가 가능하도록 root-commit이 된 코드                      |
  | develop(main)           | feature branch로 나뉘거나, main 개발 진행                    |
  | feature branch(support) | 기능별 브랜치, 기능반영 또는 드랍시 브랜치 삭제              |
  | relese branch(support)  | 개발 완료 후 QA/test를 통해 minor bug fix 등 반영            |
  | hotfix(support)         | 긴급반영 bug fix용, release는 다음버전 hotfix는 현재버전을 위함. |

  

## Github flow



#### 기본원칙

1. master는 배포가 가능한 상태여야 한다.
2. feature는 각 기능의 의도를 알 수 있도록 생성한다.
3. commit messages는 매우 중요, 명확하게 작성한다
4. pull request를 통해 협업
5.  변경사항 반영하려면 , master에 병합(**pull request**)한다.



#### Github 협업 방식

- 저장소 소유권이 `있는` 경우(shared repository)

  1. 각 유저가 저장소의 소유권이 있는 상태로 clone하여 로컬에 복제

  2. 유저들은 feature branch를 기능별 명확히 생성 후 작업

  3. 작업 완료 후 저장소에 브랜치를 push하여 저장소에 반영

  4. 저장소에 모인 브랜치를  pull request로 병합

  5. 병합된 브랜치는 저장소에서 삭제

  6. 각 유저는 master로 checkout 후 저장소에서 pull

  7. 병합된 작업이 각 유저의 로컬에 반영되면 로컬의 feature branch 삭제 
  8. 동일 유저들로 새로운 작업시 2번부터 반복.



- 저장소 소유권이 `없는` 경우(fork & pull)
  1. 소유권이 없는 저장소를 fork하여 본인의 저장소로 복제
  2. 본인 저장소에 fork된 저장소를 clone하여 로컬에 복제
  3. 작업을 위해 로컬에 브랜치 생성 
  4. 완료 후 본인 저장소로 push하여 반영
  5. 소유권자에게 pull request를 보냄
  6. 소유권자가 병합을 하면 본인 저장소의 브랜치 삭제
  7. 로컬에서 master로 checkout
  8. 소유권자의 저장소와 본인 저장소를 fetch upstream 
  9. 저장소의 내용을 로컬에 pull
  10. 새로운 작업은 3번부터 반복