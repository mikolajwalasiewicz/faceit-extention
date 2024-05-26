from playwright.sync_api import sync_playwright

with sync_playwright () as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto("https://konto.onet.pl/signin?state=https%3A%2F%2Fpoczta.onet.pl%2FSzukaj%2FEB4VBCBNQUthJVdd&client_id=poczta.onet.pl.front.onetapi.pl")
    page.get_by_label("accept and close").click()
    page.get_by_label("Adres email").click()
    page.get_by_label("Adres email").click()
    page.get_by_label("Adres email").fill("aleksander15@vp.pl")
    page.get_by_label("Hasło").click()
    page.get_by_label("Hasło").fill("xekcyc-0rukki-cyhBur")
    page.get_by_role("button", name="Dalej").click()
    page.get_by_role("button", name="Pomiń").click()
    page.get_by_placeholder("Szukaj wiadomości").click()
    page.get_by_placeholder("Szukaj wiadomości").fill("wysłane")
    page.get_by_placeholder("Szukaj wiadomości").press("Enter")
    page.locator(".row-content").first.click()
    page.frame_locator("iframe[title=\"Detal wiadomości\"]").get_by_text("Inpost Paczkomat ZGT01M Zą").click()
    with page.expect_popup() as page2_info:
        page.frame_locator("iframe[title=\"Detal wiadomości\"]").get_by_text("Przedmioty są dostarczane").click()
    page2 = page2_info.value
    page2.close()
    with page.expect_popup() as page3_info:
        page.frame_locator("iframe[title=\"Detal wiadomości\"]").get_by_text("Przedmioty są dostarczane").click()
    page3 = page3_info.value
    page.frame_locator("iframe[title=\"Detal wiadomości\"]").get_by_role("cell", name="Potwierdzenie wysyłki Zamówienie nr 405-3133031-1765163", exact=True).click()



#i want to get strings from every iframe