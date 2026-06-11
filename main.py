# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20510 안도율
# 프로젝트 주제: 업무 우선순위 정하기 및 관리해주는 프로그램

# ============================================================
# 사용 안내
# ------------------------------------------------------------
# 이 파일은 예시 골격입니다.
# 그대로 제출하지 말고, 반드시 자신의 주제에 맞게 수정하세요.
#
# 필수 조건
# 1. 2차원 리스트 사용
# 2. 함수 2개 이상, 가능하면 3개 이상 분리
# 3. 조건문 사용
# 4. 반복문 사용
# 5. 실행 결과 출력
# ============================================================


# ------------------------------------------------------------
# 1. 데이터 준비: 2차원 리스트
# ------------------------------------------------------------
# 현재 열의 의미:
# 0번 열: 업무 이름 (문자열)
# 1번 열: 마감까지 남은 일수 (정수)
# 2번 열: 업무 중요도 (1~5 정수)
# 3번 열: 계산된 우선순위 점수 (정수)
# ------------------------------------------------------------

task_list = [
    ["시장조사 보고서", 5, 4, 35],
    ["예산안 수립", 2, 5, 48],
    ["팀 회의 준비", 1, 2, 19],
    ["고객 피드백 정리", 7, 3, 23],
]


# ------------------------------------------------------------
# 2. 함수 정의
# ------------------------------------------------------------

def show_intro():
    """프로그램 제목과 안내를 출력한다."""
    print("=" * 40)
    print("💼 경영 효율화를 위한 업무 우선순위 관리기 💼")
    print("= 20510 안도율 프로젝트 =")
    print("=" * 40)

def calculate_score(days, importance):
    """중요도와 남은 일수를 바탕으로 우선순위 점수를 계산한다."""
    score = (importance * 10) - days
    return score

def get_user_input():
    """사용자에게 새로운 업무 정보를 입력받는다."""
    name = input("새로운 업무 이름을 입력하세요: ")
    days = int(input("마감까지 남은 일수를 입력하세요: "))
    importance = int(input("업무 중요도를 입력하세요 (1~5): "))
    
    if importance < 1 or importance > 5:
        print("⚠️ 오류: 중요도는 1부터 5 사이의 숫자만 입력할 수 있습니다.")
        return None, None, None
        
    return name, days, importance


def add_task(data, name, days, importance):
    if name is None:
        return data
        
    score = calculate_score(days, importance)
    
    new_task = [name, days, importance, score]
    
    data.append(new_task)
    
    print(f"\n✅ '{name}' 업무가 성공적으로 등록되었습니다!")
    return data


def show_priority_list(data):
    """2차원 리스트의 업무들을 점수가 높은 순서대로 화면에 예쁘게 출력한다."""
    print("\n💼 [현재 업무 우선순위 목록] 💼")

    if len(data) == 0:
        print("현재 등록된 업무가 없습니다. 새로운 업무를 등록해 주세요.")
        return

    data.sort(key=lambda x: x[3], reverse=True)

    for index, task in enumerate(data, start=1):
        task_name = task[0]
        task_days = task[1]
        task_importance = task[2]
        task_score = task[3]
        
        print(f"{index}위. {task_name} (마감까지: {task_days}일, 중요도: {task_importance}점) -> [우선순위 점수: {task_score}점]")


def main():
    show_intro()
    
    while True:
        print("\n--- 📌 메뉴를 선택하세요 ---")
        print("1. 새로운 업무 등록하기")
        print("2. 업무 우선순위 목록 보기")
        print("3. 프로그램 종료하기")
        
        choice = input("원하는 메뉴 번호를 입력하세요: ")
        
        if choice == "1":
            name, days, importance = get_user_input()
            add_task(task_list, name, days, importance)
            
        elif choice == "2":
            show_priority_list(task_list)
            
        elif choice == "3":
            print("\n💼 프로그램을 종료합니다. 오늘도 효율적인 하루 보내세요!")
            break
            
        else:
            print("⚠️ 잘못된 번호입니다. 1, 2, 3번 중에서만 입력해 주세요.")

# ------------------------------------------------------------
# 3. 프로그램 실행
# ------------------------------------------------------------
main()
