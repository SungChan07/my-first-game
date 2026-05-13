# 11주차 실습 기록

## 오늘 한 것
- PyInstaller 설치 및 기본 빌드 성공
- `resource_path()` 함수를 추가하여 경로 문제 해결
- `--add-data` 옵션을 사용하여 모든 에셋(이미지, 사운드)을 .exe에 포함
- 외부 폴더에서도 단독 실행되는 것 확인

## resource_path()를 써야 하는 이유
- PyInstaller의 `--onefile` 빌드는 실행 시 파일을 임시 폴더에 압축 해제함.
- 따라서 일반적인 상대경로로는 파일을 찾을 수 없기 때문에, 임시 폴더 경로인 `sys._MEIPASS`를 참조하는 `resource_path()` 함수가 반드시 필요함.

## 빌드 명령어
- --onefile --windowed --add-data "knight.png;." --add-data "bomb.png;." --add-data "red_bomb.png;." --add-data "heart.png;." --add-data "parry_knight.png;." --add-data "parry_sound.mp3;." --add-data "laser_sound.mp3;." --add-data "bomb_sound.mp3;." --add-data "heart_sound.mp3;." --add-data "choose_sound.mp3;." --add-data "gameover_sound.mp3;." --add-data "gaming_bgm1.mp3;." --add-data "gaming_bgm2.mp3;." --add-data "bgm.mp3;." --name="ParryKing" parry_king.py

## AI 활용 내역
- 경로 오류 디버깅 및 전체 코드 구조 수정에 활용
- .exe에서 이미지와 사운드를 정상적으로 출력시키기 위해 코드를 수정할 때 활용