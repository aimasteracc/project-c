"""
Project C - Main Program
使用 Project A 和 Project B 的代码生成新内容
"""

import sys
import json
from pathlib import Path
from datetime import datetime

# Fix Windows encoding issue
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 导入 submodules 中的代码
sys.path.insert(0, str(Path(__file__).parent / "project-a"))
sys.path.insert(0, str(Path(__file__).parent / "project-b"))

from lib import process_data, get_config, filter_positive
from utils import transform, reverse_text, validate_output, count_words

def generate_content():
    """使用 A 和 B 的代码生成新内容"""

    # 从项目 A 获取配置
    config = get_config()
    print(f"Config from Project A: {config}")

    # 使用项目 A 处理数据
    data = [-2, -1, 0, 1, 2, 3, 4, 5]
    processed = process_data(data)
    positive_only = filter_positive(processed)

    # 使用项目 B 转换文本
    text = "hello world from github actions"
    transformed = transform(text)
    reversed_text = reverse_text(text)
    word_count = count_words(text)

    # 组合生成结果
    result = {
        "config": config,
        "input_data": data,
        "processed_data": processed,
        "positive_values": positive_only,
        "original_text": text,
        "transformed_text": transformed,
        "reversed_text": reversed_text,
        "word_count": word_count,
        "generated_at": datetime.now().isoformat(),
        "generation_summary": {
            "total_input_items": len(data),
            "processed_items": len(processed),
            "positive_items": len(positive_only),
            "text_length": len(text),
            "words": word_count
        }
    }

    # 验证输出
    if not validate_output(transformed):
        raise ValueError("Output validation failed")

    # 保存到文件
    output_path = Path(__file__).parent / "output" / "result.json"
    output_path.parent.mkdir(exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*50}")
    print("GENERATION COMPLETE")
    print(f"{'='*50}")
    print(f"Output saved to: {output_path}")
    print(f"Config: {config['source']} v{config['version']}")
    print(f"Processed {len(data)} items, {len(positive_only)} positive")
    print(f"Text: '{text}' -> '{transformed}'")
    print(f"{'='*50}\n")

    return result

if __name__ == "__main__":
    try:
        result = generate_content()
        print("✓ Content generated successfully")
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)
