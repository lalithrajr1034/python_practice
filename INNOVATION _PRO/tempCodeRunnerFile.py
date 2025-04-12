            if not self.maximize_window():
                print("[WARNING] Could not maximize WhatsApp window. Proceeding anyway.")
            return True
        except Exception as e:
            print(f"[ERROR] Launching WhatsApp: {e}")
            return False
