import sys
import pandas as pd

def main():
    file_path = r"C:\Drop\Drop.xlsb"  # 필요 시 절대경로 유지

    # 엑셀 파일 로드
    drop_info = pd.read_excel(file_path, sheet_name="Drop_Info", engine="pyxlsb")
    drop_group = pd.read_excel(file_path, sheet_name="Drop_Group", engine="pyxlsb")
    drop_item = pd.read_excel(file_path, sheet_name="Drop_Item", engine="pyxlsb")

    def get_item_indexes(monster_id):
        # 1) Monster ID → Group IDs
        monster_rows = drop_info[drop_info.iloc[:, 0].astype(str) == str(monster_id)]
        group_ids = []
        for _, row in monster_rows.iterrows():
            group_cols = row.iloc[6::2]
            group_ids.extend([str(gid) for gid in group_cols if gid != 0 and not pd.isna(gid)])
        group_ids = list(set(group_ids))

        # 2) Group ID → Item IDs
        item_ids = []
        for gid in group_ids:
            group_rows = drop_group[drop_group.iloc[:, 0].astype(str) == str(gid)]
            for _, row in group_rows.iterrows():
                item_cols = row.iloc[2::2]
                item_ids.extend([int(iid) for iid in item_cols if iid != 0 and not pd.isna(iid)])
        item_ids = list(set(item_ids))

        # 3) Item ID → 인게임 index
        indexes = drop_item[drop_item.iloc[:, 0].isin(item_ids)].iloc[:, 3].unique().tolist()

        # 출력
        print(f"\n✅ Monster ID: {monster_id}")
        print(f"✅ Group IDs({len(group_ids)}개): {group_ids}")
        print(f"✅ Item IDs({len(item_ids)}개): {item_ids}")
        print(f"✅ Indexes({len(indexes)}개):")
        for idx in indexes:
            print(f"  - {idx}")
        print("-" * 40)

        return indexes

    # ✅ 무한 반복 입력
    while True:
        monster_id = input("Monster ID를 입력하세요 (종료하려면 'exit' 입력): ")
        if monster_id.lower() == "exit":
            print("프로그램을 종료합니다.")
            break
        get_item_indexes(monster_id)

if __name__ == "__main__":
    main()
