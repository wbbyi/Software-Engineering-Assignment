import coverage
import unittest
import os
# ----------------------------
# 1. 初始化覆盖率统计
# ----------------------------
cov = coverage.Coverage(
    source=["gui", "shapes"],  # 指定要统计的源代码包
    omit=["*/__init__.py"]     # 忽略 __init__.py 文件
)
cov.start()

# ----------------------------
# 2. 自动发现并运行所有单元测试
# ----------------------------
print("=== 正在执行单元测试 ===\n")
loader = unittest.TestLoader()
suite = loader.discover("test")  # 自动发现 test 目录下所有 test_*.py 文件
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# ----------------------------
# 3. 停止统计并保存结果
# ----------------------------
cov.stop()
cov.save()

# ----------------------------
# 4. 控制台打印覆盖率报告
# ----------------------------
print("\n=== 覆盖率报告 (终端版) ===\n")
cov.report(show_missing=True)

# ----------------------------
# 5. 生成 HTML 可视化报告
# ----------------------------
report_dir = os.path.join(os.getcwd(), "coverage_html_report")
cov.html_report(directory=report_dir)
print(f"\nHTML 报告已生成：{report_dir}\\index.html")

# ----------------------------
# 6. 自动打开报告（可选）
# ----------------------------
try:
    import webbrowser
    webbrowser.open(f"file:///{report_dir}/index.html")
except Exception:
    pass

# ----------------------------
# 7. 显示测试结果概览
# ----------------------------
if result.wasSuccessful():
    print("\n所有单元测试通过！")
else:
    print("\n部分测试失败，请检查上方输出。")
