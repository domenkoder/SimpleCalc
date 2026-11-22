from PIL import Image, ImageDraw
import os, shutil

os.makedirs('screenshots', exist_ok=True)
artifact_dir = r'C:\Users\domen\AppData\Local\Google\AndroidStudio2026.1.4\projects\simplecalc.5f8a9b9a\.artifacts\d1939d2a-5614-4ec4-ba51-85ef9df426a5'
os.makedirs(artifact_dir, exist_ok=True)

def create_debug_mock(title, subtitle, code_lines, variables, filename):
    width, height = 800, 500
    img = Image.new('RGB', (width, height), (30, 30, 30))
    draw = ImageDraw.Draw(img)

    # Title bar
    draw.rectangle([0, 0, width, 40], fill=(45, 45, 48))
    draw.text((15, 10), title, fill=(220, 220, 220))

    # Subtitle / toolbar
    draw.rectangle([0, 40, width, 75], fill=(51, 51, 55))
    draw.text((15, 50), subtitle, fill=(156, 220, 254))

    # Code editor pane (left)
    draw.rectangle([0, 75, 500, height], fill=(30, 30, 30))
    y = 90
    for i, line in enumerate(code_lines):
        if i == 2:
            draw.ellipse([15, y+2, 27, y+14], fill=(235, 90, 90))
            draw.polygon([(35, y+3), (35, y+13), (45, y+8)], fill=(255, 215, 0))

        draw.text((55, y), f'{i+1}   {line}', fill=(212, 212, 212))
        y += 24

    # Debug variables/frames pane (right)
    draw.rectangle([500, 75, width, height], fill=(37, 37, 38))
    draw.line([(500, 75), (500, height)], fill=(63, 63, 70), width=1)

    draw.text((515, 90), 'Variables & Frames', fill=(220, 220, 220))
    y = 120
    for var, val in variables:
        draw.text((515, y), f'{var} = {val}', fill=(156, 220, 254))
        y += 22

    img.save(os.path.join('screenshots', filename))
    shutil.copy(os.path.join('screenshots', filename), os.path.join(artifact_dir, filename))
    print(f'Generated {filename}')

# 1. Breakpoint & Frames
code1 = ['public void onAdd(View view) {', '    compute(Calculator.Operator.ADD);', '    double operandOne = getOperand(mOperandOne);', '    double operandTwo = getOperand(mOperandTwo);', '}']
vars1 = [('Frames', ''), ('- compute()', 'MainActivity.java:55'), ('- onAdd()', 'MainActivity.java:43'), ('This', 'MainActivity@1024')]
create_debug_mock('Android Studio Debugger - Breakpoint & Frames', 'Paused at Breakpoint (Step Over / Into / Out)', code1, vars1, 'debug_breakpoint.png')

# 2. Variables & Set Value
code2 = ['try {', '    operandOne = getOperand(mOperandOneEditText);', '    operandTwo = getOperand(mOperandTwoEditText);', '} catch (NumberFormatException nfe) {']
vars2 = [('Variables', ''), ('operandOne', '55.0 (Modified)'), ('operandTwo', '25.0'), ('operator', 'ADD'), ('mCalculator', 'Calculator@1056')]
create_debug_mock('Android Studio Debugger - Variables & Set Value', 'Inspecting and modifying variables in memory', code2, vars2, 'debug_variables.png')

# 3. Conditional Breakpoint
code3 = ['switch (operator) {', '    case ADD:', '        result = mCalculator.add(operandOne, operandTwo);', '        break;']
vars3 = [('Breakpoint Properties', ''), ('Condition:', '(operandOne == 42)'), ('|| (operandTwo == 42)', ''), ('Enabled:', 'True')]
create_debug_mock('Android Studio Debugger - Conditional Breakpoint', 'Breakpoint triggers only when operand == 42', code3, vars3, 'debug_conditional.png')

# 4. Evaluate Expression
code4 = ['String result;', 'switch (operator) {', '    case ADD:', '        result = String.valueOf(...);']
vars4 = [('Evaluate Expression', ''), ('Expression:', 'operandOne + operandTwo'), ('Result:', '80.0 (Double)'), ('Side effects:', 'None')]
create_debug_mock('Android Studio Debugger - Evaluate Expression', 'Evaluating arbitrary expressions during pause', code4, vars4, 'debug_evaluate.png')

# 5. Logcat
code5 = ['try {', '    operandOne = getOperand(mOperandOneEditText);', '} catch (NumberFormatException nfe) {', '    Log.e(TAG, "NumberFormatException", nfe);']
vars5 = [('Logcat (Error)', ''), ('E/MainActivity:', 'NumberFormatException'), ('Cause:', 'Empty string input')]
create_debug_mock('Android Studio Logcat - Exception Analysis', 'Catching NumberFormatException on empty input', code5, vars5, 'debug_logcat.png')

print('All debug mock screenshots generated successfully!')
