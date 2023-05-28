import os
import random
import sys

groupA = [
    ["Li", "Na", "K", "Rb", "Cs", "Fr"],
    ["Be", "Mg", "Ca", "Sr", "Ba", "Ra"],
    ["B", "Al", "Ga", "In", "Tl", "Nh"],
    ["C", "Si", "Ge", "Sn", "Pb", "Fl"],
    ["N", "P", "As", "Sb", "Bi", "Mc"],
    ["O", "S", "Se", "Te", "Po", "Lv"],
    ["F", "Cl", "Br", "I", "At", "Ts"],
    ["He", "Ne", "Ar", "Kr", "Xe", "Rn", "Og"]
]

transition = [
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn"
]

names = {
    "Li": "ลิเทียม",
    "Na": "โซเดียม",
    "K": "โพแทสเซียม",
    "Rb": "รูบิเดียม",
    "Cs": "เซเซียม",
    "Fr": "ฟรานเซียม",
    "Be": "เบอริลเลียม",
    "Mg": "แมกนีเซียม",
    "Ca": "แคลเซียม",
    "Sr": "สตรอนเทียม",
    "Ba": "แบเรียม",
    "Ra": "แรเดียม",
    "B": "โบรอน",
    "Al": "อะลูมิเนียม",
    "Ga": "แกลเลียม",
    "In": "อินเดียม",
    "Tl": "แทลเลียม",
    "Nh": "นิฮอเนียม",
    "C": "คาร์บอน",
    "Si": "ซิลิกอน",
    "Ge": "เจอร์เมเนียม",
    "Sn": "ทิน",
    "Pb": "ลีด/ตะกั่ว",
    "Fl": "ฟลิโรเวี่ยม",
    "N": "ไนโตรเจน",
    "P": "ฟอสฟอรัส",
    "As": "อาร์เซนิก",
    "Sb": "แอนติโมนี",
    "Bi": "บิสมัท",
    "Mc": "โมสโกเนียม",
    "O": "ออกซิเจน",
    "S": "ซัลเฟอร์/กำมะถัน",
    "Se": "เซเลเนียม",
    "Te": "เทลลูเรียม",
    "Po": "โพโลเนียม",
    "Lv": "ลิเวอเรียม",
    "F": "ฟลูออรีน",
    "Cl": "คลอรีน",
    "Br": "บรอมีน",
    "I": "ไอโอดีน",
    "At": "แอสไทนีน",
    "Ts": "เทนเนสซีน",
    "He": "ฮีเลียม",
    "Ne": "นีออน",
    "Ar": "อาร์กอน",
    "Kr": "คริปตอน",
    "Xe": "ซีนอน",
    "Rn": "เรดอน",
    "Og": "โอกาเนสซอน",
    "Sc": "สแกนเดียม",
    "Ti": "ไทเทเนียม",
    "V": "วานาเดียม",
    "Cr": "โครเมียม",
    "Mn": "แมงกานีส",
    "Fe": "ไอรอน/เหล็ก",
    "Co": "โคบอลท์",
    "Ni": "นิเกิล",
    "Cu": "คอปเปอร์/ทองแดง",
    "Zn": "ซิงค์/สังกะสี"
}

prompt = ('"Group A"\n'
          '"Li" "Na" "K" "Rb" "Cs" "Fr"\n'
          '"Be" "Mg" "Ca" "Sr" "Ba" "Ra"\n'
          '"B" "Al" "Ga" "In" "Tl" "Nh"\n'
          '"C" "Si" "Ge" "Sn" "Pb" "Fl"\n'
          '"N" "P" "As" "Sb" "Bi" "Mc"\n'
          '"O" "S" "Se" "Te" "Po" "Lv"\n'
          '"F" "Cl" "Br" "I" "At" "Ts"\n'
          '"He" "Ne" "Ar" "Kr" "Xe" "Rn" "Og"\n'
          '"Transition"\n'
          '"Sc" "Ti" "V" "Cr" "Mn" "Fe" "Co" "Ni" "Cu" "Zn"')

index = 0
index2 = 0

print('Cr.Kittipat')
print(prompt)

answer = input("คุณจำเสร็จแล้วหรือยัง (y/n): ")

if answer.lower() == "y":
    os.system('clear')
    while index < len(groupA):
        group = groupA[index]
        for i, element in enumerate(group):
            X = input(f"ธาตุ (หมู่ที่ {index + 1}, ลำดับที่ {i + 1}): ")

            if X == element:
                print(f"ถูกต้อง ({names[X]})")
            else:
                print("ธาตุที่ระบุไม่ถูกต้อง")
                sys.exit()  
        index += 1

    if index == len(groupA):
        print("มึงตอบถูกต้องทุกธาตุในกลุ่ม A")
        os.system('clear')

    while index2 < len(transition):
        V = input(f"Transition (ลำดับที่ {index2 + 1}): ")

        if V == transition[index2]:
            print(f"ถูกต้อง ({names[V]})")
            index2 += 1
        else:
            print(random.choice(["ผิด", "ไม่ถูกไอควาย", "โง่จริง", "กลับไปทำใหม่นะจ๊ะ"]))
            sys.exit()  

    if index2 == len(transition):
        print("คุณตอบถูกต้องทุกธาตุแล้ว เย่ๆ")

        print("ธาตุที่ตอบถูกต้องในกลุ่ม A:")
        for group in groupA:
            for element in group:
                print(names[element])
        print("ธาตุ Transition ที่ตอบถูกต้อง:")
        for element in transition:
            print(names[element])
