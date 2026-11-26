// Nœuds Blueprint pour connaître le clavier du joueur

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "SteezyKeyboardLibrary.generated.h"

UCLASS()
class STEEZYKEYBOARD_API USteezyKeyboardLibrary : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()

public:
	// Vrai quand le clavier choisi dans Windows a A et Z sur les deux premières touches en haut à gauche
	UFUNCTION(BlueprintPure, Category = "Steezy|Clavier", meta = (DisplayName = "Is Azerty Keyboard"))
	static bool IsAzertyKeyboard();

	// Les lettres des deux premières touches en haut à gauche, par exemple AZ en AZERTY ou QW en QWERTY
	UFUNCTION(BlueprintPure, Category = "Steezy|Clavier", meta = (DisplayName = "Get Top Left Letters"))
	static FString GetTopLeftLetters();
};
