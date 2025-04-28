from figures import Triangle, Rectangle, Trapeze, Parallelogram, Circle

def parse_figure(line):
    parts = line.strip().split()
    figure_type = parts[0]
    params = list(map(int, parts[1:]))

    if figure_type == 'Triangle':
        return Triangle(*params)
    elif figure_type == 'Rectangle':
        return Rectangle(*params)
    elif figure_type == 'Trapeze':
        return Trapeze(*params)
    elif figure_type == 'Parallelogram':
        return Parallelogram(*params)
    elif figure_type == 'Circle':
        return Circle(*params)
    else:
        raise ValueError(f"Unknown figure type: {figure_type}")

def process_file(filename):
    figures = []
    with open(filename, 'r') as f:
        for line in f:
            if line.strip():
                try:
                    figure = parse_figure(line)
                    figures.append(figure)
                except Exception as e:
                    print(f"Error parsing line: {line.strip()} - {e}")

    if not figures:
        print("No valid figures found.")
        return

    max_area_figure = max(figures, key=lambda f: f.area())
    max_perimeter_figure = max(figures, key=lambda f: f.perimeter())

    print(f"\nФайл: {filename}")
    print(f"Фігура з найбільшою площею має площу: {max_area_figure.area():.2f} і периметр: {max_area_figure.perimeter():.2f}")
    print(f"Фігура з найбільшим периметром має периметр: {max_perimeter_figure.perimeter():.2f} і площу: {max_perimeter_figure.area():.2f}")

if __name__ == "__main__":
    filenames = [
        "inputs/input01.txt",
        "inputs/input02.txt",
        "inputs/input03.txt",
    ]

    for file in filenames:
        process_file(file)
