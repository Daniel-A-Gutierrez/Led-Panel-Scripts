import ledpanel

print("testing existing functionality")
ledpanel.LightUpColumn(15, ledpanel.blue)
ledpanel.LightUpRow(14, (128,128,128))
ledpanel.ScrollPanelRGB("sansbobina", 128,0,128,3)

print("testing new functionality")
for i in range(0,1024,2):
    ledpanel.SetPixel(i //32 , i%32 , i//5, 0, 255-1//5)

ledpanel.clearPanel()