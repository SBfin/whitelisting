# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:49:52 2022

@author: silvi
"""

TRUSTABLE_FOLLOWERS = ["0x2E21f5d32841cf8C7da805185A041400bF15f21A", 
                       "0x42a578e3557f5854B27D48E7d753fEb2f428546D",
                        "0x6C77a5a88C0AE712BAeABE12FeA81532060dcBf5",
                        "0x0550730EDb1948d3170113FF4FA0e4770fA47401",
                        "0x3B3acEa1fCCe64eaf8B9d4bcD1Dc11F7302B5Fb8",
                        "0x343Ea18bd524775feDE0F10E9230073DbD1b437d",
                        "0x2E21f5d32841cf8C7da805185A041400bF15f21A",
                        "0x4A1a2197f307222cD67A1762D9A352F64558d9Be",
                        "0xa408DDD1BeA8f798449e79C0e8A25d8b301e526b",
                        "0x42a578e3557f5854B27D48E7d753fEb2f428546D",
                        "0xcde3725B25D6d9bC78CF0941cC15Fd9710c764b9",
                        "0xcA1F6d7d8E902617f8Bdd87866e00f9844C40a77",
                        "0xd3B307753097430FaEdFdb89809610bF8e8f3203",
                        "0x3A5bd1E37b099aE3386D13947b6a90d97675e5e3",
                        "0x34915628fc56aE8FF6684be39462e7ba398164b8",
                        "0x50F92b07d2Fd316e6b301445031A4A90469521a3",
                        "0xa0751bec519b2C096cB29C428e16131D1C1d2141",
                        "0xB9f771AA2F126CB1a52eC973abD73c8661684060",
                        "0x2388AC2Dd7082012Ac4fcD31884ACCf1Db602816",
                        "0x89fd020648E3162BfEeA36BcC0f0b022E08a788D",
                        "0xD1f1f8c40a61d11d153935c17D38D6db9465f842",
                        "0x52EAF3F04cbac0a4B9878A75AB2523722325D4D4",
                        "0xe4AdE213224Fec51C80bcCcDCC5033F7248CA736",
                        "0x7F748CdACd7eB1D3E48a0f2118CB45Cf95d18b5f",
                        "0x67D2c5E0c19AfdCBa7E3AAd3D10A07F82C167106",
                        "0x06F455e2C297a4Ae015191FA7A4A11C77c5b1b7c",
                        "0xd52e3603f313C253f470524f8Ce9690282DCf86a",
                        "0x4691dB13AA194048A6f6b4431d632b6979cAcAd3",
                        "0x79C44097BcCa05232fbAaA2F88c7217042A714FB",
                        "0x422938990FED07aEb904260b1094943afC2e366d",
                        "0xaFB2735179C625dD1D199b415a88A32C5D0fcCCE",
                        "0x9487404e560b830408bD76C8534B3901fC8FeF85",
                        "0x2d24a18e8311ADF75B154E2eC298C2779c1af7a9",
                        "0xD822e9DC8c3b77eB8DAEF45C00d127e23AFa4A7E",
                        "0x1e904dB986C7223bFE75083e84A8800956574504",
                        "0x8eC94086A724cbEC4D37097b8792cE99CaDCd520",
                        "0xc98F11DAAAC76D3ef368fDF54fbbA34FfD951976",
                        "0xC04AA40079430465d2C102Ef4436B8Fcf63058AE",
                        "0x705A42EcC5dF243BF9298f1D091b89761522a796",
                        "0xD6FCD2F85fE975bB9b0f3C1B1c6802bB09d33E43",
                        "0xD3069C9e486A8b77aDD55ae3ceB3A4b138Fb76c7",
                        "0xA94f8e818f8347ea28F893552F6Ecb61eD343CEc",
                        "0x3b8C52e12f7De23e603A45d0c456Ac075B5c69F1",
                        "0x4b8BBf8a7fF7e01019AFcD760aD730E1827492F0",
                        "0x01d79BcEaEaaDfb8fD2F2f53005289CFcF483464",
                        "0xaFB2735179C625dD1D199b415a88A32C5D0fcCCE",
                        "0xF01Cc7154e255D20489E091a5aEA10Bc136696a8",
                        "0x0eb44361be820882ee8A587A4b64c16290F90aD3",
                        "0x259cC22956b3a8d872bc180E2b86a8dE9126f028",
                        "0x5d8b04E983a2f83174530A3574E89F42E5Ee066E",
                        "0x072e83cdE5c102fDCF32BE328034E1bB2DADCB01",
                        "0x55A7bA485178B80f251e7ADea34110540083F4Ba",
                        "0xC13Da0f3701CbfbbA6744E513ea9d3eaBdC1c588",
                        "0xb095B85cA3298A881b95022a4CEecAde67172916",
                        "0x16238F07A1819c746B8F9196060245e616D6026c",
                        "0xA83444576F86C8B59A542eC2F286a19aB12c2666",
                        "0x437739E9f7774B73361eAa487ea593Ce4384e260",
                        "0x248ba21F6ff51cf0CD4765C3Bc9fAD2030a591d5",
                        "0xD7b47B8Bc490724da2f022b61eecB57B146Ea8fC",
                        "0xFd37f4625CA5816157D55a5b3F7Dd8DD5F8a0C2F",
                        "0xcf7117CfccE4afB52890fEaFE2DdDcDC794487a5",
                        "0xf2Bb2785A9f29F3015375c20683b43016a8cb8e4",
                        "0xcE7571697BaE6177394717eA9C71Fca728fa6461",
                        "0x8F96aA1C4cbd3b10786c81031c6917bcaC66423c",
                        "0x2d24a18e8311ADF75B154E2eC298C2779c1af7a9",
                        "0x1334c0727eCa7B03C36bde4924B02E4665107573",
                        "0x52535FBbEDFB3fDAAfb96dC8B68b3C115998F11a",
                        "0x2D0D6A8553993a3E9eD1D86415358D1EDEfa82F1",
                        "0x66Da63B03feCA7Dd44a5bB023BB3645D3252Fa32",
                        "0x49397421fda03a7fcE9E82189c488A8945bF713d",
                        "0x844A641290d188CdDda9f7a7fe8E43d757A5BBAA",
                        "0xB3E2Eb3180BEaF883130849EF4fFAbc737C0DA8b",
                        "0x242C7f2279A3187279fD61605004A4B477B63A78",
                        "0x1B9Dba9C36724F25fb57aE62aDCD5d3d01DFec93",
                        "0x6F6783Da5d28092B33A6317bF59B58F5EAe36d88",
                        "0x8E535e856f634b570e780D204fe0bc1812C5eFC2",
                        "0xE7aC670dc7c0A7f11ad81db4163329F79F821843",
                        "0xD5F7818b117193509382E734c9C4EBB517461B9a",
                        "0x324Fbd9536bf3d77d36137310fd4abe5130DfEA9",
                        "0x9C85C376A50721c75E4E015AC22EfE066dbB73EC",
                        "0x89D3e7F71e23e584a2984e57fBF8b34fAC421e3C",
                        "0xAbD8Cee5a93265fc7D1F9e45f0169294d01B8802",
                        "0x8C7eEE2beA0452424E89097ae3cFda4d9D82035D",
                        "0xb85A29ad9d951147b68b5e3C09eA706da4315905",
                        "0xFA7Bd4B2b8Ec60b35d881131f71D364A76cAd888",
                        "0xe8265D372266F45f99FD4E13fBc0F1d7D59a12Ea",
                        "0x4eFFbA37E8C7e34Fc4241995b3380F2B9033C99f",
                        "0xf8875523CbD4226369cc7022f208f2609adC1d0E",
                        "0xeEc38A8835BF98eb8F4abee900455A5175d836A3",
                        "0xB7767355aa657b3Ed66f0de24dA5018a5E2862bd",
                        "0x7853Eabb6cFa980eBfD27e3F77e69590EA53c0b7",
                        "0xC3048079040C993818021e955b62102094cd4d03",
                        "0x26ab154C70AEC017d78E6241da76949c37b171e2",
                        "0xD4Ea8867eB3B65920716Ae6f113570e35C6f68bf",
                        "0x657359a2a5d4CE8cfbCa626974c0583D59b072cC",
                        "0x6765f946700549F784103D65001401B70ecfa588",
                        "0x5833869fdEB4D371b854D7474F5F84B43320FD05",
                        "0xd5f2FbC5E739C7f2cC68Dfa907FB66801ed3Ada8",
                        "0xE5A182aaC2CDe5B5d98b11c75eC7a0561BBe0639",
                        "0x943F37ea3a202828B472B2A46961EEd81FB0F9F5"]
