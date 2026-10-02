from pyxlsb import open_workbook

def load_sheet_as_list(file_path, sheet_name):
    """pyxlsb 시트를 2차원 리스트로 변환"""
    data = []
    with open_workbook(file_path) as wb:
        with wb.get_sheet(sheet_name) as sheet:
            for row in sheet.rows():
                data.append([cell.v for cell in row])
    return data

def main():
    file_path = r"C:\Drop\Drop.xlsb"

    # 엑셀 데이터 로드
    drop_info = load_sheet_as_list(file_path, "Drop_Info")
    drop_group = load_sheet_as_list(file_path, "Drop_Group")
    drop_item = load_sheet_as_list(file_path, "Drop_Item")

    def get_item_indexes(monster_id):
        # 1) Monster ID → Group IDs
        group_ids = set()
        for row in drop_info:
            if str(row[0]) == str(monster_id):
                for i in range(6, len(row), 2):  # G, I, K...
                    if row[i] not in (0, None):
                        group_ids.add(str(row[i]))

        # 2) Group ID → Item IDs
        item_ids = set()
        for gid in group_ids:
            for row in drop_group:
                if str(row[0]) == str(gid):
                    for i in range(2, len(row), 2):  # C, E, G...
                        if row[i] not in (0, None):
                            item_ids.add(int(row[i]))

        # 3) Item ID → 인게임 index (D열 = index 3)
        indexes = set()
        for row in drop_item:
            if row[0] in item_ids:
                indexes.add(row[3])

        # 출력
        print(f"\n✅ Monster ID: {monster_id}")
        print(f"✅ Group IDs({len(group_ids)}개): {list(group_ids)}")
        print(f"✅ Item IDs({len(item_ids)}개): {list(item_ids)}")
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
