from langbite.langbite import LangBiTe

def main():
    # Proporciona el archivo de entrada (en este caso, "mi_prueba_hf.json")
    langbite_instance = LangBiTe(file="langbite/mi_prueba_hf.json")

    # Ejecutar el flujo completo de prueba
    langbite_instance.execute_full_scenario()

if __name__ == "__main__":
    main()
