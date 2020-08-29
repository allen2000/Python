from appium import webdriver
desired_caps = dict(
    platformName='Android',
    platformVersion='9',
    app='D:/com.example.android.notepad.apk' #use the full path,suggest put in Non system root directory
)
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

txt="allen"

el2 = driver.find_element_by_id("com.example.android.notepad:id/add_note")
el2.click()
el3 = driver.find_element_by_id("com.example.android.notepad:id/note")
driver.implicitly_wait(1)
el3.send_keys(txt)
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView[2]")
el4.click()
tt = driver.find_element_by_id("com.example.android.notepad:id/noteContent")
assert tt.text==txt
driver.implicitly_wait(3)
el5 = driver.find_element_by_accessibility_id(u"更多选项")
el5.click()
el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")
el6.click()
el7 = driver.find_element_by_id("android:id/button1")
el7.click()