// Module du plugin Steezy Keyboard, il n'a besoin que des briques de base du moteur
using UnrealBuildTool;

public class SteezyKeyboard : ModuleRules
{
	public SteezyKeyboard(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
		PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine" });
	}
}
