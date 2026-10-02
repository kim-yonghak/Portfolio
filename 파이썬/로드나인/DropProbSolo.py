import sys
import pandas as pd

def main():
    file_path = r"C:\Drop\Drop.xlsb"

    drop_info = pd.read_excel(file_path, sheet_name="Drop_Info", engine="pyxlsb")
    drop_group = pd.read_excel(file_path, sheet_name="Drop_Group", engine="pyxlsb")
    drop_item = pd.read_excel(file_path, sheet_name="Drop_Item", engine="pyxlsb")

    def get_item_paths(monster_id):
        monster_rows = drop_info[drop_info.iloc[:, 0].astype(str) == str(monster_id)]

        group_prob_dict = {}

        # 1) Drop_Info → Group ID + 최소 확률 유지
        for _, row in monster_rows.iterrows():
            for i in range(5, len(row) - 1, 2):  # F열부터: 확률, ID
                prob = row.iloc[i]
                group_id = row.iloc[i + 1]
                if group_id != 0 and not pd.isna(group_id) and prob != 0 and not pd.isna(prob):
                    group_id = str(group_id)
                    prob = prob / 1000000
                    if group_id not in group_prob_dict or prob < group_prob_dict[group_id]:
                        group_prob_dict[group_id] = prob

        # 2) Drop_Group → 모든 드랍 경로 저장
        drop_results = []  # [(group_id, item_id, item_index, 확률)]
        for group_id, group_prob in group_prob_dict.items():
            group_rows = drop_group[drop_group.iloc[:, 0].astype(str) == group_id]
            for _, row in group_rows.iterrows():
                for i in range(1, len(row) - 1, 2):  # B = 1: 확률 / C = 2: Item ID
                    item_prob = row.iloc[i]
                    item_id = row.iloc[i + 1]
                    if item_id != 0 and not pd.isna(item_id) and item_prob != 0 and not pd.isna(item_prob):
                        item_id = int(item_id)
                        final_prob = group_prob * (item_prob / 1000000)
                        item_rows = drop_item[drop_item.iloc[:, 0] == item_id]
                        for _, irow in item_rows.iterrows():
                            item_index = irow.iloc[3]
                            if not pd.isna(item_index):
                                drop_results.append((group_id, item_id, int(item_index), final_prob))

        # ✅ 출력
        print(f"\n✅ Monster ID: {monster_id}")
        print(f"✅ 개별 드랍 경로 {len(drop_results)}개:")
        for group_id, item_id, item_index, prob in drop_results:
            print(f"  - Group: {group_id} → Item: {item_id} → Index: {item_index} → 확률: {round(prob * 100, 6)}%")
        print("-" * 40)

    # ✅ 무한 입력 반복
    while True:
        monster_id = input("Monster ID를 입력하세요 (종료하려면 'exit' 입력): ")
        if monster_id.lower() == "exit":
            print("프로그램을 종료합니다.")
            break
        get_item_paths(monster_id)

if __name__ == "__main__":
    main()
