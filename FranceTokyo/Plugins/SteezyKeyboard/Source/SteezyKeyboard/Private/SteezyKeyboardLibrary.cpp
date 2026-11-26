// Lecture de la disposition clavier active dans Windows

#include "SteezyKeyboardLibrary.h"

#if PLATFORM_WINDOWS
#include "Windows/AllowWindowsPlatformTypes.h"
#include <Windows.h>
#include "Windows/HideWindowsPlatformTypes.h"
#endif

FString USteezyKeyboardLibrary::GetTopLeftLetters()
{
#if PLATFORM_WINDOWS
	// Codes des touches physiques, ils ne changent pas d'un clavier à l'autre
	// 0x10 est la touche à droite de Tab, 0x11 celle juste après
	const UINT FirstKey = 0x10;
	const UINT SecondKey = 0x11;

	// Disposition que Windows applique en ce moment à la fenêtre du jeu
	const HKL Layout = GetKeyboardLayout(0);

	// Windows renvoie la lettre imprimée sur chaque touche pour cette disposition
	const UINT FirstLetter = MapVirtualKeyExW(FirstKey, MAPVK_VSC_TO_VK, Layout);
	const UINT SecondLetter = MapVirtualKeyExW(SecondKey, MAPVK_VSC_TO_VK, Layout);

	FString Letters;
	Letters.AppendChar(static_cast<TCHAR>(FirstLetter));
	Letters.AppendChar(static_cast<TCHAR>(SecondLetter));
	return Letters;
#else
	// Hors Windows on garde le clavier américain par défaut
	return TEXT("QW");
#endif
}

bool USteezyKeyboardLibrary::IsAzertyKeyboard()
{
	return GetTopLeftLetters() == TEXT("AZ");
}
