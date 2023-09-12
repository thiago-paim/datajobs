if __name__ == "__main__":
    """Sample script for testing Chrome installation and undetected_chromedriver"""
    import time

    import undetected_chromedriver as uc

    driver = uc.Chrome(headless=True, use_subprocess=False)
    driver.get("https://www.google.com")
    print(driver.title)
    time.sleep(2)
    print(driver.page_source)
    print("\nQuitting driver test...")
    time.sleep(2)
    driver.quit()
