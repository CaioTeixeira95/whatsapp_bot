import argparse
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

parser = argparse.ArgumentParser(description='Send message to contacts.')
parser.add_argument(
    '--file',
    type=str,
    required=True,
    help='File with the name and number phone from your contacts'
)

args = parser.parse_args()


def try_to_find(element, attribute, text):
    try:
        text = browser.find_element(
            By.XPATH, '//{element}[{attribute}="{text}"]'.format(
                element=element, attribute=attribute, text=text
            )
        )
        return text
    except NoSuchElementException:
        return None


def send_message():
    with open(args.file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            search_input = try_to_find(
                'input', '@title', 'Procurar ou começar uma nova conversa'
            )
            search_input.send_keys(line)
            message_text = browser.find_element_by_class_name(
                '_3u328, copyable-text, selectable-text'
            )
            message_text.send_keys('Oi {}'.format(line))
            sleep(3)


if __name__ == '__main__':
    browser = webdriver.Firefox()
    browser.get('https://web.whatsapp.com')

    text = None
    while text is None:
        text = try_to_find('h1', 'text()', 'Mantenha seu celular conectado')
        sleep(3)

    send_message()
