import sys
import pandas as pd

def main():
    file_path = r"C:\Drop\Drop.xlsb"

    drop_info = pd.read_excel(file_path, sheet_name="Drop_Info", engine="pyxlsb")
    drop_group = pd.read_excel(file_path, sheet_name="Drop_Group", engine="pyxlsb")
    drop_item = pd.read_excel(file_path, sheet_name="Drop_Item", engine="pyxlsb")

    def get_item_indexes(monster_id):
        monster_rows = drop_info[drop_info.iloc[:, 0].astype(str) == str(monster_id)]

        group_prob_dict = {}

        # ✅ 1) Drop_Info → Group ID 최저 확률만 유지
        for _, row in monster_rows.iterrows():
            for i in range(5, len(row) - 1, 2):
                prob = row.iloc[i]
                group_id = row.iloc[i + 1]
                if group_id != 0 and not pd.isna(group_id) and prob != 0 and not pd.isna(prob):
                    group_id = str(group_id)
                    prob = prob / 1000000
                    if group_id not in group_prob_dict or prob < group_prob_dict[group_id]:
                        group_prob_dict[group_id] = prob

        # ✅ 2) Drop_Group → Item ID: 경로별로 모두 저장
        results = []

        for group_id, group_prob in group_prob_dict.items():
            group_rows = drop_group[drop_group.iloc[:, 0].astype(str) == group_id]

            for _, row in group_rows.iterrows():
                for i in range(1, len(row) - 1, 2):
                    item_prob = row.iloc[i]
                    item_id = row.iloc[i + 1]
                    if item_id != 0 and not pd.isna(item_id) and item_prob != 0 and not pd.isna(item_prob):
                        item_id = int(item_id)
                        prob_val = item_prob / 1000000
                        final_prob = group_prob * prob_val

                        item_rows = drop_item[drop_item.iloc[:, 0] == item_id]
                        for _, irow in item_rows.iterrows():
                            item_index = irow.iloc[3]
                            if not pd.isna(item_index):
                                item_index = int(item_index)
                                results.append({
                                    "ItemIndex": item_index,
                                    "GroupID": group_id,
                                    "ItemID": item_id,
                                    "GroupProb": group_prob,
                                    "ItemProb": prob_val,
                                    "FinalProb": final_prob
                                })

        # ✅ 출력
        print(f"\n✅ Monster ID: {monster_id}")
        print(f"✅ 드롭 아이템 경로별 드랍률:")
        for r in results:
            percent = round(r["FinalProb"] * 100, 6)
            print(f"  - ItemIndex: {r['ItemIndex']} | GroupID: {r['GroupID']} | ItemID: {r['ItemID']} | 확률: {percent}%")
        print("-" * 40)

    # ✅ 무한 입력 반복
    while True:
        monster_id = input("Monster ID를 입력하세요 (종료하려면 'exit' 입력): ")
        if monster_id.lower() == "exit":
            print("프로그램을 종료합니다.")
            break
        get_item_indexes(monster_id)

if __name__ == "__main__":
    main()
