import math

# installed with "pip install pysvg-py3"
import pysvg.structure
import pysvg.builders

# Hilfsfunktion zum Errechnen der Offsets der x- und y-Koordinaten abhängig vom Winkel und Abstand(delta)


def get_deltas(winkel, delta):
    ratio = math.tan(winkel/180*math.pi)
    delta_x = math.sqrt(delta*delta/((ratio * ratio)+1))
    delta_y = delta_x*ratio
    return (delta_x, delta_y)

# Funktion zum Zeichnen der einzelnen Kreise; circle_number = Anzahl der Kreise; delta_pos = prozentuale Abweichung der Kreise vom Mittelpunkt
# svg_document = Vektorgrafik-Dokument; shape_builder = Klasse zum Zeichnen der Kreise in das Vektorgrafik-Dokument


def paint_circles(circle_number, delta_pos, svg_document, shape_builder):
    midpoint = 500
    center_circle_size = 200
    circle_size = 200
    delta_pos = center_circle_size * (delta_pos / 100)

    # Zeichnen des zentralen Kreises
    svg_document.addElement(shape_builder.createEllipse(
        midpoint, midpoint, str(center_circle_size)+"px", str(center_circle_size)+"px", strokewidth=1, stroke="black", fill="none"))

    for circle_count in range(0, circle_number):
        winkel = 360 / circle_number * circle_count
        winkel = winkel % 360

        if winkel >= 0 and winkel < 90:  # I. Quadrant
            winkel = 90 - winkel
            delta_pos_circle = get_deltas(winkel, delta_pos)
            svg_document.addElement(shape_builder.createEllipse(
                midpoint+delta_pos_circle[0], midpoint-delta_pos_circle[1], str(circle_size)+"px", str(circle_size)+"px", strokewidth=1, stroke="black", fill="none"))
        elif winkel > 90 and winkel < 180:  # IV. Quadrant
            winkel = winkel - 90
            delta_pos_circle = get_deltas(winkel, delta_pos)
            svg_document.addElement(shape_builder.createEllipse(
                midpoint+delta_pos_circle[0], midpoint+delta_pos_circle[1], str(circle_size)+"px", str(circle_size)+"px", strokewidth=1, stroke="black", fill="none"))
        elif winkel > 180 and winkel < 270:  # III. Quadrant
            winkel = 90 - (winkel - 180)
            delta_pos_circle = get_deltas(winkel, delta_pos)
            svg_document.addElement(shape_builder.createEllipse(
                midpoint-delta_pos_circle[0], midpoint+delta_pos_circle[1], str(circle_size)+"px", str(circle_size)+"px", strokewidth=1, stroke="black", fill="none"))
        elif winkel > 270 and winkel < 360:  # II. Quadrant
            winkel = winkel - 270
            delta_pos_circle = get_deltas(winkel, delta_pos)
            svg_document.addElement(shape_builder.createEllipse(
                midpoint-delta_pos_circle[0], midpoint-delta_pos_circle[1], str(circle_size)+"px", str(circle_size)+"px", strokewidth=1, stroke="black", fill="none"))
        elif winkel == 90:
            svg_document.addElement(shape_builder.createEllipse(
                midpoint+delta_pos, midpoint, str(circle_size)+"px", str(circle_size)+"px", strokewidth=1, stroke="black", fill="none"))
        elif winkel == 180:
            svg_document.addElement(shape_builder.createEllipse(
                midpoint, midpoint+delta_pos, str(circle_size)+"px", str(circle_size)+"px", strokewidth=1, stroke="black", fill="none"))
        elif winkel == 270:
            svg_document.addElement(shape_builder.createEllipse(
                midpoint-delta_pos, midpoint, str(circle_size)+"px", str(circle_size)+"px", strokewidth=1, stroke="black", fill="none"))
        elif winkel == 0:
            svg_document.addElement(shape_builder.createEllipse(
                midpoint, midpoint-delta_pos, str(circle_size)+"px", str(circle_size)+"px", strokewidth=1, stroke="black", fill="none"))

    # cut outging lines
    svg_document.addElement(shape_builder.createEllipse(
        midpoint, midpoint, str(center_circle_size+1)+"px", str(center_circle_size+1)+"px", strokewidth=1, stroke="white", fill="none"))
    for x in range(center_circle_size+2, center_circle_size+100):
        svg_document.addElement(shape_builder.createEllipse(
            midpoint, midpoint, str(x)+"px", str(x)+"px", strokewidth=2, stroke="white", fill="none"))


# Initialisieren der Vektorgrafik-Objekte
svg_document = pysvg.structure.Svg()
shape_builder = pysvg.builders.ShapeBuilder()

# Aufruf der Funktion zum Zeichnen der Kreise
paint_circles(3, 107, svg_document, shape_builder)

# Ausgabe der XML der Vektorgrafik
print(svg_document.getXML())

# Speichern der Vektorgrafik als Datei
svg_document.save("chipchugan_raw.svg")
