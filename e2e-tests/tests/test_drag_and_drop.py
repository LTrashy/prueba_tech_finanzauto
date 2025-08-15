from selenium.webdriver.common.by import By

def test_drag_and_drop(driver):
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    source = driver.find_element(By.ID, "column-a")
    target = driver.find_element(By.ID, "column-b")
    driver.execute_script("""
        function createEvent(typeOfEvent) {
          var event = document.createEvent("CustomEvent");
          event.initCustomEvent(typeOfEvent, true, true, null);
          event.dataTransfer = {
            data: {},
            setData: function (key, value) { this.data[key] = value; },
            getData: function (key) { return this.data[key]; }
          };
          return event;
        }
        function dispatchEvent(element, event, transferData) {
          if (transferData) { event.dataTransfer = transferData; }
          if (element.dispatchEvent) { element.dispatchEvent(event); }
          else if (element.fireEvent) { element.fireEvent("on" + event.type, event); }
        }
        var source = arguments[0];
        var target = arguments[1];
        var dragStartEvent = createEvent('dragstart');
        dispatchEvent(source, dragStartEvent);
        var dropEvent = createEvent('drop');
        dispatchEvent(target, dropEvent, dragStartEvent.dataTransfer);
        var dragEndEvent = createEvent('dragend');
        dispatchEvent(source, dragEndEvent, dragStartEvent.dataTransfer);
    """, source, target)
    assert target.find_element(By.TAG_NAME, "header").text == "A"
