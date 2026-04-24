import docx
import re
import os

def clean_text(text):
    if not text:
        return ""
    text = text.strip()
    text = re.sub(r'\n\s*\n', '\n', text)
    text = re.sub(r'\s*/\s*', '/', text)
    text = re.sub(r'\s*-\s*', '-', text)
    
    return text

def extract_text_from_table(table):
    table_text = []
    for row in table.rows:
        row_data = []
        for cell in row.cells:
            cell_text = clean_text(cell.text)
            if cell_text not in row_data:
                row_data.append(cell_text)
        if any(row_data):
            table_text.append(" - ".join(row_data))
    return "\n".join(table_text)

def process_word_file(input_docx, output_txt):
    try:
        doc = docx.Document(input_docx)
    except Exception as e:
        print(f"Lỗi khi đọc file Word: {e}")
        return

    target_keys = [
        "TÊN THỦ TỤC", "MÃ THỦ TỤC", "SỐ QUYẾT ĐỊNH", "CẤP", "LOẠI THỦ TỤC",
        "CƠ QUAN", "LĨNH VỰC", "ĐỐI TƯỢNG", "CƠ QUAN CÓ THẨM QUYỀN",
        "CƠ QUAN PHỐI HỢP", "CƠ QUAN ĐƯỢC ỦY QUYỀN", "ĐỊA CHỈ TIẾP NHẬN",
        "THỜI HẠN", "TRÌNH TỰ", "CÁCH THỨC THỰC HIỆN", "HỒ SƠ", "ĐIỀU KIỆN",
        "KẾT QUẢ", "PHÁP LÝ (CHI TIẾT)", "PHÁP LÝ (RÚT GỌN)", "TỪ KHÓA", 
        "MÔ TẢ", "CÂU HỎI THƯỜNG GẶP"
    ]

    extracted_data = {key: [] for key in target_keys}
    current_key = None

    for element in doc.element.body:
        text_content = ""
        
        if element.tag.endswith('p'):
            paragraph = docx.text.paragraph.Paragraph(element, doc)
            text_content = clean_text(paragraph.text)
            
        elif element.tag.endswith('tbl'):
            table = docx.table.Table(element, doc)
            text_content = extract_text_from_table(table)

        if not text_content:
            continue

        is_key = False
        for key in target_keys:
            if text_content.upper().startswith(key):
                current_key = key
                is_key = True
                
                value_part = text_content[len(key):].strip(': ')
                if value_part:
                    extracted_data[current_key].append(value_part)
                break
        
        if text_content.upper().startswith("KEYWORDS") or text_content.upper().startswith("SEARCH_HINT"):
            current_key = "IGNORE"
            continue

        if not is_key and current_key and current_key != "IGNORE":
            extracted_data[current_key].append(text_content)

    with open(output_txt, 'w', encoding='utf-8') as f:
        for key in target_keys:
            f.write(f"### {key}:\n")
            
            content_lines = extracted_data[key]
            if not content_lines:
                f.write("Không có thông tin\n")
            else:
                final_content = "\n".join(content_lines)
                final_content = clean_text(final_content)
                f.write(f"{final_content}\n")
            
            f.write("\n")

    print(f"Đã xử lý xong! Dữ liệu được lưu tại: {output_txt}")

if __name__ == "__main__":
    input_file = "105698.doc" 
    output_file = "du_lieu_chuan_hoa.txt"
    
    if os.path.exists(input_file):
        process_word_file(input_file, output_file)
    else:
        print(f"Không tìm thấy file: {input_file}")