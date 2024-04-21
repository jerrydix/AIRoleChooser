# TODO(developer): Vertex AI SDK - uncomment below & run
# pip3 install --upgrade --user google-cloud-aiplatform
# gcloud auth application-default login

import vertexai
from vertexai.generative_models import GenerativeModel
from nicegui import ui

response = ""
specializations = ["Мелкий бытовой ремонт – Врезка замков",
                       "Мелкий бытовой ремонт – Мелкие внутренние или уличные малярные работы",
                       "Мелкий бытовой ремонт – Мелкие столярные работы",
                       "Мелкий бытовой ремонт – Мелкий ремонт напольных покрытий",
                       "Мелкий бытовой ремонт – Мелкий ремонт облицовки зданий",
                       "Мелкий бытовой ремонт – Монтаж и ремонт карнизов, плинтусов, жалюзи",
                       "Мелкий бытовой ремонт – Установка дверей", "Сантехник – Монтаж и ремонт полотенцесушителя",
                       "Сантехник – Монтаж и ремонт смесителей",
                       "Сантехник – Монтаж, ремонт или перенос сантехнических коммуникаций, труб, узлов",
                       "Сантехник – Подключение стиральных, посудомоечных машин", "Сантехник – Прочистка засоров",
                       "Сантехник – Срочные аварийные работы", "Сантехник – Установка душевой кабины",
                       "Сантехник – Установка санфаянса - ванны, раковины, унитаза",
                       "Сборщик - монтажник – Мелкий ремонт мебели",
                       "Сборщик - монтажник – Навеска картин, полок, фурнитуры",
                       "Сборщик - монтажник – Сборка и монтаж мебельных систем - кухонь, мебельных стенок",
                       "Сборщик - монтажник – Сборка мебели - шкафов, комодов, стеллажей", "Уборщик - дворник – Глажка",
                       "Уборщик - дворник – Мойка окон",
                       "Уборщик - дворник – Поддерживающая или генеральная уборка помещений",
                       "Уборщик - дворник – Уборка после ремонта", "Уборщик - дворник – Уборка придомовой территории",
                       "Уборщик - дворник – Чистка бассейнов или других водоемов",
                       "Цветовод - садовод – Лечение и реабилитация зеленых насаждений",
                       "Цветовод - садовод – Регулярный уход за зелёными насаждениями, домашними растениями",
                       "Цветовод - садовод – Сезонная или санитарная обрезка деревьев и кустарников",
                       "Цветовод - садовод – Сезонный уход за зелёными насаждениями - открытие, закрытие сезона",
                       "Электрик – Монтаж осветительных приборов",
                       "Электрик – Подведение проводки к месту подключения электроприборов",
                       "Электрик – Ремонт автоматических ворот и калиток", "Электрик – Ремонт бытовой техники",
                       "Электрик – Ремонт уличного освещения", "Электрик – Срочные аварийные работы",
                       "Электрик – Устранение неисправностей в выключателях, розетках, осветительных приборах",
                       "Электрик – Устранение неисправностей в щитке",
                       "Электрик – Устранение скрытых неисправностей в проводке"]

with ui.column().classes('w-full items-center justify-center h-screen'):

    ui.label("LLM Spec Chooser").style('font-size: 24px').style('font-weight: bold')
    with ui.row():
        inputField = ui.input(placeholder="Enter task...").props('rounded outlined dense')
        ui.button("Go").on_click(lambda: select_specialization("aimasterchooser", "europe-west3", inputField.value)).props('rounded')

    responseLabel = ui.label(response)

ui.run(host="0.0.0.0", port=6969, dark=True, title="LLM Spec Chooser")

def select_specialization(project_id: str, location: str, prompt: str) -> str:
    print("PROMPT:" + prompt)
    vertexai.init(project=project_id, location=location)
    multimodal_model = GenerativeModel("gemini-pro-vision")

    prompt = (
            f"Задача: \"{prompt}\"\nИз следующего списка специализаций разнорабочего выбери ту, которая лучше всего описывает задачу, и в качестве ответа дай только одну выбранную специализацию. Если ни одна специализация не подходит под задачу напиши \"Error: No suitable spec found\".\nСписок специализаций:\n")

    global specializations
    for i in specializations:
        prompt += "- " + i + "\n"

    output = multimodal_model.generate_content(
        [
            # Part.from_uri(
            #   "gs://generativeai-downloads/images/scones.jpg", mime_type="image/jpeg"
            # ),
            prompt
        ]
    )

    print(output)
    result = output.text
    if result not in specializations and result != "Error: No suitable spec found":
        result = "Error: No suitable spec found"
    global response, responseLabel
    responseLabel.text = result

