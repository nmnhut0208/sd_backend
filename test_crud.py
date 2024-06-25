import requests


payload = {
                        "alwayson_scripts": {
                            "ControlNet": {
                            "args": [
                                {
                                "advanced_weighting": None,
                                "batch_images": "",
                                "control_mode": "Balanced",
                                "enabled": True,
                                "guidance_end": 1,
                                "guidance_start": 0,
                                "hr_option": "Both",
                                "image": None,
                                "inpaint_crop_input_image": False,
                                "input_mode": "simple",
                                "is_ui": True,
                                "loopback": False,
                                "low_vram": False,
                                "model": "control_v11p_sd15_canny [d14c016b]",
                                "module": "canny",
                                "output_dir": "",
                                "pixel_perfect": True,
                                "processor_res": 512,
                                "resize_mode": "Crop and Resize",
                                "save_detected_map": True,
                                "threshold_a": 100,
                                "threshold_b": 200,
                                "weight": 1
                                },
                                {
                                "advanced_weighting": None,
                                "batch_images": "",
                                "control_mode": "Balanced",
                                "enabled": False,
                                "guidance_end": 1,
                                "guidance_start": 0,
                                "hr_option": "Both",
                                "image": None,
                                "inpaint_crop_input_image": False,
                                "input_mode": "simple",
                                "is_ui": True,
                                "loopback": False,
                                "low_vram": False,
                                "model": "None",
                                "module": "none",
                                "output_dir": "",
                                "pixel_perfect": False,
                                "processor_res": -1,
                                "resize_mode": "Crop and Resize",
                                "save_detected_map": True,
                                "threshold_a": -1,
                                "threshold_b": -1,
                                "weight": 1
                                },
                                {
                                "advanced_weighting": None,
                                "batch_images": "",
                                "control_mode": "Balanced",
                                "enabled": False,
                                "guidance_end": 1,
                                "guidance_start": 0,
                                "hr_option": "Both",
                                "image": None,
                                "inpaint_crop_input_image": False,
                                "input_mode": "simple",
                                "is_ui": True,
                                "loopback": False,
                                "low_vram": False,
                                "model": "None",
                                "module": "none",
                                "output_dir": "",
                                "pixel_perfect": False,
                                "processor_res": -1,
                                "resize_mode": "Crop and Resize",
                                "save_detected_map": True,
                                "threshold_a": -1,
                                "threshold_b": -1,
                                "weight": 1
                                }
                            ]
                            },
                            "Extra options": {
                            "args": []
                            },
                            "Hypertile": {
                            "args": []
                            },
                            "Refiner": {
                            "args": [
                                False,
                                "",
                                0.8
                            ]
                            },
                            "Seed": {
                            "args": [
                                -1,
                                False,
                                -1,
                                0,
                                0,
                                0
                            ]
                            }
                        },
                        "batch_size": 1,
                        "cfg_scale": 7,
                        "comments": {},
                        "denoising_strength": 0.5,
                        "disable_extra_networks": False,
                        "do_not_save_grid": False,
                        "do_not_save_samples": False,
                        "height": 512,
                        "image_cfg_scale": 1.5,
                        "init_images": [""],
                        "initial_noise_multiplier": 1,
                        "inpaint_full_res": 0,
                        "inpaint_full_res_padding": 32,
                        "inpainting_fill": 1,
                        "inpainting_mask_invert": 0,
                        "mask_blur": 4,
                        "mask_blur_x": 4,
                        "mask_blur_y": 4,
                        "n_iter": 1,
                        "negative_prompt": "six fingers, deformity, extra fingers, deformed hands,, walks backwards, ugly, deformed, noisy, blurred, hands next to the face, distorted, out of focus, bad anatomy, extra limbs, bad face, bad hands, bad face, low quality body, worse quality body, bad body, bad anatomy drawing, mutation hands, mutation fingers, extra fingers, missing fingers, watermark, nsfw, (lack of clothes:1.2), (lack of detail:1.2), nsfw",
                        "override_settings": {
                                "sd_model_checkpoint": "asianrealisticSdlife_v40-fp16-no-ema.safetensors [36604d7196]"
                        },
                        "override_settings_restore_afterwards": True,
                        "prompt": "A woman all in blue, blue eyes, pretty makeup, (big blue flower in hair:1.2), (blue eye shadow makeup palettem:1.2), facial closeup, beautiful jewlery, focus on eyes, beautiful smile, white teeth, HD image, 4k, perfect small detaill",
                        "resize_mode": 0,
                        "restore_faces": False,
                        "s_churn": 0,
                        "s_min_uncond": 0,
                        "s_noise": 1,
                        "s_tmax": None,
                        "s_tmin": 0,
                        "sampler_name": "DPM++ 2M",
                        "script_args": [],
                        "script_name": None,
                        "seed": 1888041100,
                        "seed_enable_extras": True,
                        "seed_resize_from_h": -1,
                        "seed_resize_from_w": -1,
                        "steps": 20,
                        "styles": [],
                        "subseed": -1,
                        "subseed_strength": 0.3,
                        "tiling": False,
                        "width": 512
                        }

url = "http://localhost:8111/backend/crud/update_by_style/Sweety"

# method put
response = requests.put(url, json={"img_url": "abc.jpg"})

print(response.json())